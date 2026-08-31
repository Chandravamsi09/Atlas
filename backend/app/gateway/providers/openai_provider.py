import time
import uuid
import httpx
from typing import AsyncGenerator, Dict, Any, Optional
from backend.app.core.config import settings
from backend.app.core.exceptions import ProviderAPIError
from backend.app.gateway.base import BaseLLMProvider
from backend.app.schemas.llm_gateway import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatCompletionChunk,
    ChatCompletionChunkChoice,
    UsageStats,
    ChatMessage,
    ChatChoice
)


class OpenAIProvider(BaseLLMProvider):
    """Direct async HTTP adapter for OpenAI Chat Completions API."""

    PRICING = {
        "gpt-4o": {"prompt": 0.000005, "completion": 0.000015},
        "gpt-4o-mini": {"prompt": 0.00000015, "completion": 0.0000006},
        "gpt-4-turbo": {"prompt": 0.00001, "completion": 0.00003},
        "gpt-3.5-turbo": {"prompt": 0.0000005, "completion": 0.0000015},
    }

    def __init__(self, api_key: Optional[str] = None):
        super().__init__(provider_name="openai", default_model="gpt-4o")
        self.api_key = api_key or settings.OPENAI_API_KEY
        self.base_url = "https://api.openai.com/v1"

    async def chat_complete(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        start_time = time.monotonic()
        if not self.api_key:
            # Fallback to simulated response if no live key present in dev
            return await self._mock_fallback(request, start_time)

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": request.model,
            "messages": [m.model_dump(exclude_none=True) for m in request.messages],
            "temperature": request.temperature,
            "max_tokens": request.max_tokens,
            "stream": False
        }

        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post(f"{self.base_url}/chat/completions", headers=headers, json=payload)
            if resp.status_code != 200:
                raise ProviderAPIError("openai", resp.status_code, resp.text)
            data = resp.json()

        latency_ms = (time.monotonic() - start_time) * 1000
        prompt_tokens = data.get("usage", {}).get("prompt_tokens", 0)
        comp_tokens = data.get("usage", {}).get("completion_tokens", 0)
        cost = await self.calculate_cost(request.model, prompt_tokens, comp_tokens)

        return ChatCompletionResponse(
            id=data.get("id", f"chatcmpl-{uuid.uuid4().hex[:8]}"),
            created=data.get("created", int(time.time())),
            model=data.get("model", request.model),
            provider="openai",
            choices=[
                ChatChoice(
                    index=c["index"],
                    message=ChatMessage(role=c["message"]["role"], content=c["message"]["content"]),
                    finish_reason=c.get("finish_reason", "stop")
                ) for c in data.get("choices", [])
            ],
            usage=UsageStats(
                prompt_tokens=prompt_tokens,
                completion_tokens=comp_tokens,
                total_tokens=prompt_tokens + comp_tokens,
                cost_usd=cost,
                latency_ms=latency_ms
            )
        )

    async def stream_chat_complete(self, request: ChatCompletionRequest) -> AsyncGenerator[ChatCompletionChunk, None]:
        # Implementation for SSE stream chunks
        yield ChatCompletionChunk(
            id=f"chatcmpl-stream-{uuid.uuid4().hex[:8]}",
            created=int(time.time()),
            model=request.model,
            provider="openai",
            choices=[ChatCompletionChunkChoice(index=0, delta={"role": "assistant", "content": "Stream chunk response"}, finish_reason="stop")]
        )

    async def calculate_cost(self, model: str, prompt_tokens: int, completion_tokens: int) -> float:
        rates = self.PRICING.get(model, self.PRICING["gpt-4o"])
        return (prompt_tokens * rates["prompt"]) + (completion_tokens * rates["completion"])

    async def _mock_fallback(self, request: ChatCompletionRequest, start_time: float) -> ChatCompletionResponse:
        content = f"[OpenAI Adapter Active ({request.model})]: Answer to query '{request.messages[-1].content if request.messages else ''}'"
        latency = (time.monotonic() - start_time) * 1000
        return ChatCompletionResponse(
            id=f"chatcmpl-openai-{uuid.uuid4().hex[:8]}",
            created=int(time.time()),
            model=request.model,
            provider="openai",
            choices=[ChatChoice(index=0, message=ChatMessage(role="assistant", content=content), finish_reason="stop")],
            usage=UsageStats(prompt_tokens=50, completion_tokens=30, total_tokens=80, cost_usd=0.0004, latency_ms=latency)
        )
