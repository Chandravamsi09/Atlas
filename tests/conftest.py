import pytest
import asyncio
from backend.app.schemas.llm_gateway import ChatCompletionRequest, ChatMessage


@pytest.fixture
def sample_chat_request() -> ChatCompletionRequest:
    return ChatCompletionRequest(
        model="gpt-4o",
        messages=[
            ChatMessage(role="system", content="You are a helpful assistant."),
            ChatMessage(role="user", content="Explain quantum computing in one sentence.")
        ],
        temperature=0.7,
        max_tokens=100
    )
