from fastapi import APIRouter, Depends, HTTPException
from backend.app.api.deps import get_current_user_and_tenant, require_permission
from backend.app.core.rbac import Scope
from backend.app.schemas.llm_gateway import ChatCompletionRequest, ChatCompletionResponse
from backend.app.gateway.router import smart_router
from backend.app.guardrails.pipeline import guardrail_pipeline
from backend.app.gateway.cache.semantic_cache import global_semantic_cache
from backend.app.observability.trace_store import global_trace_store

router = APIRouter()


@router.post("/chat/completions", response_model=ChatCompletionResponse, tags=["LLM Gateway"])
async def create_chat_completion(
    request: ChatCompletionRequest,
    auth_data = Depends(require_permission(Scope.MODELS_INVOKE))
):
    user, org_id, role = auth_data
    user_prompt_text = request.messages[-1].content if request.messages else ""

    # 1. Guardrail input validation & PII scrubbing
    if request.guardrails_enabled and request.messages:
        last_msg = request.messages[-1]
        last_msg.content = guardrail_pipeline.process_input(last_msg.content)

    # 2. Check Semantic Cache
    cached = None
    if request.enable_cache:
        cached = await global_semantic_cache.get(request)
        if cached:
            # Record trace for cached response
            global_trace_store.record_trace(
                endpoint="/api/v1/chat/completions",
                model=cached.model,
                duration_ms=cached.usage.latency_ms if cached.usage else 5.0,
                prompt_tokens=cached.usage.prompt_tokens if cached.usage else 0,
                completion_tokens=cached.usage.completion_tokens if cached.usage else 0,
                total_tokens=cached.usage.total_tokens if cached.usage else 0,
                cost_usd=0.0,
                status="200 OK (Cache Hit)",
                tenant_id=org_id,
                user_prompt=user_prompt_text,
                model_response=cached.choices[0].message.content if cached.choices else "",
                cache_hit=True
            )
            return cached

    # 3. Smart routing to provider
    response = await smart_router.route_chat_completion(request)

    # 4. Guardrail output validation
    if request.guardrails_enabled and response.choices:
        response.choices[0].message.content = guardrail_pipeline.process_output(
            response.choices[0].message.content
        )

    # 5. Populate cache
    if request.enable_cache:
        await global_semantic_cache.set(request, response)

    # 6. Record Trace in Observability Store
    model_output_text = response.choices[0].message.content if response.choices else ""
    latency = response.usage.latency_ms if response.usage else 210.0
    p_tokens = response.usage.prompt_tokens if response.usage else 25
    c_tokens = response.usage.completion_tokens if response.usage else 30
    t_tokens = response.usage.total_tokens if response.usage else (p_tokens + c_tokens)
    cost = response.usage.cost_usd if response.usage else 0.00001

    trace_entry = global_trace_store.record_trace(
        endpoint="/api/v1/chat/completions",
        model=response.model,
        duration_ms=latency,
        prompt_tokens=p_tokens,
        completion_tokens=c_tokens,
        total_tokens=t_tokens,
        cost_usd=cost,
        status="200 OK",
        tenant_id=org_id,
        user_prompt=user_prompt_text,
        model_response=model_output_text,
        cache_hit=False
    )

    return response
