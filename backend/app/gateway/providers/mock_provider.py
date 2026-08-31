import asyncio
import time
import uuid
from typing import AsyncGenerator, Dict, Any
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


class MockLLMProvider(BaseLLMProvider):
    """Mock LLM Provider for high-speed local testing, benchmarking, and unit suites."""
    
    def __init__(self):
        super().__init__(provider_name="mock", default_model="mock-gpt-4o")

    async def chat_complete(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        start_time = time.monotonic()
        await asyncio.sleep(0.01) # Simulated network latency
        
        last_msg = request.messages[-1].content if request.messages else "Hello!"
        content = f"[Mock response from {request.model}]: Echoing: {last_msg}"
        
        prompt_tokens = sum(self.estimate_tokens(m.content) for m in request.messages)
        comp_tokens = self.estimate_tokens(content)
        latency = (time.monotonic() - start_time) * 1000

        return ChatCompletionResponse(
            id=f"chatcmpl-mock-{uuid.uuid4().hex[:8]}",
            created=int(time.time()),
            model=request.model,
            provider="mock",
            choices=[ChatChoice(index=0, message=ChatMessage(role="assistant", content=content), finish_reason="stop")],
            usage=UsageStats(
                prompt_tokens=prompt_tokens,
                completion_tokens=comp_tokens,
                total_tokens=prompt_tokens + comp_tokens,
                cost_usd=0.00001,
                latency_ms=latency
            )
        )

    async def stream_chat_complete(self, request: ChatCompletionRequest) -> AsyncGenerator[ChatCompletionChunk, None]:
        last_msg = request.messages[-1].content if request.messages else "Hello!"
        words = f"[Mock stream from {request.model}]: Echoing: {last_msg}".split(" ")
        req_id = f"chatcmpl-mock-{uuid.uuid4().hex[:8]}"

        for i, word in enumerate(words):
            await asyncio.sleep(0.005)
            chunk = ChatCompletionChunk(
                id=req_id,
                created=int(time.time()),
                model=request.model,
                provider="mock",
                choices=[ChatCompletionChunkChoice(index=0, delta={"role": "assistant", "content": word + " "}, finish_reason=None if i < len(words) - 1 else "stop")]
            )
            yield chunk

    async def calculate_cost(self, model: str, prompt_tokens: int, completion_tokens: int) -> float:
        return (prompt_tokens * 0.000005) + (completion_tokens * 0.000015)
