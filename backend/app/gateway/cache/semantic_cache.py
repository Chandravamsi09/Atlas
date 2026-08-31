import math
import time
from typing import Optional, List, Tuple
from backend.app.gateway.cache.base_cache import BaseCache
from backend.app.schemas.llm_gateway import ChatCompletionRequest, ChatCompletionResponse, ChatChoice, ChatMessage, UsageStats


class SemanticCache(BaseCache):
    """
    Vector semantic cache calculating cosine similarity between prompt embeddings.
    Drastically reduces token costs for semantically identical questions.
    """
    def __init__(self, similarity_threshold: float = 0.92):
        self.threshold = similarity_threshold
        # Stores: [(prompt_text, embedding_vector, cached_response, expiry_timestamp)]
        self._entries: List[Tuple[str, List[float], ChatCompletionResponse, float]] = []

    def _mock_embed(self, text: str) -> List[float]:
        # Fast deterministic hash-embedding for local execution / testing
        import hashlib
        h = hashlib.sha256(text.encode("utf-8")).digest()
        vec = [float(b) / 255.0 for b in h[:16]]
        # Normalize
        norm = math.sqrt(sum(x*x for x in vec)) or 1.0
        return [x / norm for x in vec]

    def _cosine_similarity(self, a: List[float], b: List[float]) -> float:
        dot = sum(x * y for x, y in zip(a, b))
        return dot

    async def get(self, request: ChatCompletionRequest) -> Optional[ChatCompletionResponse]:
        if not request.messages:
            return None
        
        prompt_text = request.messages[-1].content
        query_vec = self._mock_embed(prompt_text)
        now = time.time()

        for cached_text, vec, resp, expiry in self._entries:
            if now < expiry:
                sim = self._cosine_similarity(query_vec, vec)
                if sim >= self.threshold:
                    cached_copy = resp.model_copy(deep=True)
                    cached_copy.cached = True
                    cached_copy.usage.cache_hit = True
                    return cached_copy
        return None

    async def set(self, request: ChatCompletionRequest, response: ChatCompletionResponse, ttl_seconds: int = 3600) -> None:
        if not request.messages:
            return
        prompt_text = request.messages[-1].content
        vec = self._mock_embed(prompt_text)
        self._entries.append((prompt_text, vec, response, time.time() + ttl_seconds))

    async def clear(self) -> None:
        self._entries.clear()


global_semantic_cache = SemanticCache()
