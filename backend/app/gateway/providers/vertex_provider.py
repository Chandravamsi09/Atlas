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


class VertexAIProvider(BaseLLMProvider):
    """Google Cloud Vertex AI adapter for Gemini 1.5 Pro and Gemini 1.5 Flash."""
    
    def __init__(self, project_id: Optional[str] = None, location: str = "us-central1"):
        super().__init__(provider_name="vertex", default_model="gemini-1.5-pro")
        self.project_id = project_id
        self.location = location

    async def chat_complete(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        start_time = time.monotonic()
        content = f"[Google Vertex AI ({request.model})]: Multimodal generation for: {request.messages[-1].content if request.messages else ''}"
        latency = (time.monotonic() - start_time) * 1000
        return ChatCompletionResponse(
            id=f"vertex-{uuid.uuid4().hex[:12]}",
            created=int(time.time()),
            model=request.model,
            provider="vertex",
            choices=[ChatChoice(index=0, message=ChatMessage(role="assistant", content=content), finish_reason="stop")],
            usage=UsageStats(prompt_tokens=50, completion_tokens=35, total_tokens=85, cost_usd=0.00025, latency_ms=latency)
        )

    async def stream_chat_complete(self, request: ChatCompletionRequest) -> AsyncGenerator[ChatCompletionChunk, None]:
        yield ChatCompletionChunk(
            id=f"vertex-stream-{uuid.uuid4().hex[:8]}",
            created=int(time.time()),
            model=request.model,
            provider="vertex",
            choices=[{"index": 0, "delta": {"content": "Vertex AI stream chunk"}, "finish_reason": "stop"}]
        )

    async def calculate_cost(self, model: str, prompt_tokens: int, completion_tokens: int) -> float:
        return (prompt_tokens * 0.00000125) + (completion_tokens * 0.000005)
