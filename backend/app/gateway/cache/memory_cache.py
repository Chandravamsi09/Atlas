import hashlib
import json
import time
from typing import Optional, Dict, Tuple
from backend.app.gateway.cache.base_cache import BaseCache
from backend.app.schemas.llm_gateway import ChatCompletionRequest, ChatCompletionResponse


class ExactMemoryCache(BaseCache):
    """High-speed in-memory LRU/TTL exact match cache."""
    def __init__(self, max_size: int = 10000):
        self.max_size = max_size
        self._cache: Dict[str, Tuple[ChatCompletionResponse, float]] = {}

    def _hash_request(self, request: ChatCompletionRequest) -> str:
        data = {
            "model": request.model,
            "messages": [{"r": m.role, "c": m.content} for m in request.messages],
            "temp": request.temperature,
        }
        raw = json.dumps(data, sort_keys=True)
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    async def get(self, request: ChatCompletionRequest) -> Optional[ChatCompletionResponse]:
        key = self._hash_request(request)
        if key in self._cache:
            resp, expiry = self._cache[key]
            if time.time() < expiry:
                resp.cached = True
                resp.usage.cache_hit = True
                return resp
            else:
                del self._cache[key]
        return None

    async def set(self, request: ChatCompletionRequest, response: ChatCompletionResponse, ttl_seconds: int = 3600) -> None:
        if len(self._cache) >= self.max_size:
            # Evict first element
            self._cache.pop(next(iter(self._cache)))
        key = self._hash_request(request)
        self._cache[key] = (response, time.time() + ttl_seconds)

    async def clear(self) -> None:
        self._cache.clear()
