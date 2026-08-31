from fastapi import APIRouter, Depends, HTTPException
from backend.app.api.deps import get_current_user_and_tenant, require_permission
from backend.app.core.rbac import Scope
from backend.app.schemas.llm_gateway import ChatCompletionRequest, ChatCompletionResponse
from backend.app.gateway.router import smart_router
from backend.app.guardrails.pipeline import guardrail_pipeline
from backend.app.gateway.cache.semantic_cache import global_semantic_cache

router = APIRouter()


@router.post("/chat/completions", response_model=ChatCompletionResponse, tags=["LLM Gateway"])
async def create_chat_completion(
    request: ChatCompletionRequest,
    auth_data = Depends(require_permission(Scope.MODELS_INVOKE))
):
    user, org_id, role = auth_data

    # 1. Guardrail input validation & PII scrubbing
    if request.guardrails_enabled and request.messages:
        last_msg = request.messages[-1]
        last_msg.content = guardrail_pipeline.process_input(last_msg.content)

    # 2. Check Semantic Cache
    if request.enable_cache:
        cached = await global_semantic_cache.get(request)
        if cached:
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

    return response
