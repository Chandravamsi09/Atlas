import pytest
import asyncio
from backend.app.gateway.cache.semantic_cache import global_semantic_cache
from backend.app.schemas.llm_gateway import ChatCompletionRequest, ChatCompletionResponse, ChatChoice, ChatMessage, UsageStats


def test_semantic_cache_hit():
    req1 = ChatCompletionRequest(
        model="gpt-4o",
        messages=[ChatMessage(role="user", content="What is the capital of France?")]
    )
    resp1 = ChatCompletionResponse(
        id="resp-1",
        created=12345,
        model="gpt-4o",
        provider="mock",
        choices=[ChatChoice(index=0, message=ChatMessage(role="assistant", content="Paris"), finish_reason="stop")],
        usage=UsageStats(prompt_tokens=10, completion_tokens=5, total_tokens=15)
    )
    
    asyncio.run(global_semantic_cache.set(req1, resp1))
    cached_resp = asyncio.run(global_semantic_cache.get(req1))
    assert cached_resp is not None
    assert cached_resp.cached is True
    assert cached_resp.usage.cache_hit is True
