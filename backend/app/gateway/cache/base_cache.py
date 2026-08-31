import abc
from typing import Optional, Any
from backend.app.schemas.llm_gateway import ChatCompletionRequest, ChatCompletionResponse


class BaseCache(abc.ABC):
    @abc.abstractmethod
    async def get(self, request: ChatCompletionRequest) -> Optional[ChatCompletionResponse]:
        pass

    @abc.abstractmethod
    async def set(self, request: ChatCompletionRequest, response: ChatCompletionResponse, ttl_seconds: int = 3600) -> None:
        pass

    @abc.abstractmethod
    async def clear(self) -> None:
        pass
