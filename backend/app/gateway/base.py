import time
import abc
from typing import AsyncGenerator, Dict, Any, List, Optional
from backend.app.schemas.llm_gateway import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatCompletionChunk,
    UsageStats,
    ChatMessage,
    ChatChoice
)


class BaseLLMProvider(abc.ABC):
    """Abstract base interface for downstream LLM provider adapters."""
    
    def __init__(self, provider_name: str, default_model: str):
        self.provider_name = provider_name
        self.default_model = default_model

    @abc.abstractmethod
    async def chat_complete(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        """Executes a non-streaming chat completion request."""
        pass

    @abc.abstractmethod
    async def stream_chat_complete(self, request: ChatCompletionRequest) -> AsyncGenerator[ChatCompletionChunk, None]:
        """Executes a streaming SSE chat completion request."""
        pass

    @abc.abstractmethod
    async def calculate_cost(self, model: str, prompt_tokens: int, completion_tokens: int) -> float:
        """Calculates USD cost based on provider token pricing schedule."""
        pass

    def estimate_tokens(self, text: str) -> int:
        """Heuristic / tiktoken approximation for prompt tokens (4 chars ~ 1 token)."""
        return max(1, len(text) // 4)
