import pytest
import asyncio
from backend.app.gateway.router import smart_router
from backend.app.schemas.llm_gateway import ChatCompletionRequest, ChatMessage


def test_smart_router_fallback(sample_chat_request):
    response = asyncio.run(smart_router.route_chat_completion(sample_chat_request))
    assert response is not None
    assert len(response.choices) > 0
    assert response.usage.total_tokens > 0
