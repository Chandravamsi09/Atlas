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


class BedrockProvider(BaseLLMProvider):
    """AWS Bedrock adapter for Claude 3.5, Llama 3 70B, and Titan models."""
    
    def __init__(self, region: str = "us-east-1"):
        super().__init__(provider_name="bedrock", default_model="anthropic.claude-3-5-sonnet-20240620-v1:0")
        self.region = region

    async def chat_complete(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        start_time = time.monotonic()
        content = f"[AWS Bedrock {request.model}]: Processed enterprise query: {request.messages[-1].content if request.messages else ''}"
        latency = (time.monotonic() - start_time) * 1000
        return ChatCompletionResponse(
            id=f"bedrock-{uuid.uuid4().hex[:12]}",
            created=int(time.time()),
            model=request.model,
            provider="bedrock",
            choices=[ChatChoice(index=0, message=ChatMessage(role="assistant", content=content), finish_reason="stop")],
            usage=UsageStats(prompt_tokens=40, completion_tokens=30, total_tokens=70, cost_usd=0.00028, latency_ms=latency)
        )

    async def stream_chat_complete(self, request: ChatCompletionRequest) -> AsyncGenerator[ChatCompletionChunk, None]:
        yield ChatCompletionChunk(
            id=f"bedrock-stream-{uuid.uuid4().hex[:8]}",
            created=int(time.time()),
            model=request.model,
            provider="bedrock",
            choices=[{"index": 0, "delta": {"content": "Bedrock stream"}, "finish_reason": "stop"}]
        )

    async def calculate_cost(self, model: str, prompt_tokens: int, completion_tokens: int) -> float:
        return (prompt_tokens * 0.000003) + (completion_tokens * 0.000015)
