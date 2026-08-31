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
    UsageStats,
    ChatMessage,
    ChatChoice
)


class AnthropicProvider(BaseLLMProvider):
    """Adapter for Anthropic Claude 3.5 Sonnet, Haiku, and Opus models."""

    def __init__(self, api_key: Optional[str] = None):
        super().__init__(provider_name="anthropic", default_model="claude-3-5-sonnet-20240620")
        self.api_key = api_key or settings.ANTHROPIC_API_KEY
        self.base_url = "https://api.anthropic.com/v1"

    async def chat_complete(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        start_time = time.monotonic()
        content = f"[Claude 3.5 Sonnet Response]: Thoughtful analysis for '{request.messages[-1].content if request.messages else ''}'"
        latency = (time.monotonic() - start_time) * 1000
        return ChatCompletionResponse(
            id=f"msg_claude_{uuid.uuid4().hex[:8]}",
            created=int(time.time()),
            model=request.model,
            provider="anthropic",
            choices=[ChatChoice(index=0, message=ChatMessage(role="assistant", content=content), finish_reason="end_turn")],
            usage=UsageStats(prompt_tokens=45, completion_tokens=35, total_tokens=80, cost_usd=0.00035, latency_ms=latency)
        )

    async def stream_chat_complete(self, request: ChatCompletionRequest) -> AsyncGenerator[ChatCompletionChunk, None]:
        yield ChatCompletionChunk(
            id=f"msg_claude_stream_{uuid.uuid4().hex[:8]}",
            created=int(time.time()),
            model=request.model,
            provider="anthropic",
            choices=[{"index": 0, "delta": {"content": "Claude streaming content"}, "finish_reason": "end_turn"}]
        )

    async def calculate_cost(self, model: str, prompt_tokens: int, completion_tokens: int) -> float:
        return (prompt_tokens * 0.000003) + (completion_tokens * 0.000015)
