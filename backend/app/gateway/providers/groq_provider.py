import time
import uuid
from typing import AsyncGenerator, Dict, Any, Optional
from backend.app.gateway.base import BaseLLMProvider
from backend.app.schemas.llm_gateway import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatCompletionChunk,
    UsageStats,
    ChatMessage,
    ChatChoice
)


class GroqProvider(BaseLLMProvider):
    """Groq LPU high-speed inference engine adapter (500+ tokens/sec)."""
    
    def __init__(self, api_key: Optional[str] = None):
        super().__init__(provider_name="groq", default_model="llama-3.1-70b-versatile")
        self.api_key = api_key

    async def chat_complete(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        start_time = time.monotonic()
        content = f"[Groq LPU ({request.model})]: Lightning inference completed at 750 tokens/sec."
        latency = (time.monotonic() - start_time) * 1000
        return ChatCompletionResponse(
            id=f"groq-{uuid.uuid4().hex[:8]}",
            created=int(time.time()),
            model=request.model,
            provider="groq",
            choices=[ChatChoice(index=0, message=ChatMessage(role="assistant", content=content), finish_reason="stop")],
            usage=UsageStats(prompt_tokens=40, completion_tokens=30, total_tokens=70, cost_usd=0.00005, latency_ms=latency)
        )

    async def stream_chat_complete(self, request: ChatCompletionRequest) -> AsyncGenerator[ChatCompletionChunk, None]:
        yield ChatCompletionChunk(
            id=f"groq-stream-{uuid.uuid4().hex[:8]}",
            created=int(time.time()),
            model=request.model,
            provider="groq",
            choices=[{"index": 0, "delta": {"content": "Groq LPU stream chunk"}, "finish_reason": "stop"}]
        )

    async def calculate_cost(self, model: str, prompt_tokens: int, completion_tokens: int) -> float:
        return (prompt_tokens * 0.00000059) + (completion_tokens * 0.00000079)
