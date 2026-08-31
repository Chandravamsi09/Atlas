import time
import asyncio
from typing import Optional, Dict, Tuple
from backend.app.core.exceptions import RateLimitExceededError


class TokenBucketRateLimiter:
    """
    In-memory / Redis-backed high performance Leaky Token Bucket rate limiter.
    Enforces requests-per-second (RPS), burst limits, and token-per-minute (TPM).
    """
    def __init__(self, rps: float = 100.0, burst: int = 200, tpm: int = 1_000_000):
        self.rps = rps
        self.burst = burst
        self.tpm = tpm
        self._buckets: Dict[str, Tuple[float, float]] = {} # key -> (tokens, last_time)
        self._token_buckets: Dict[str, Tuple[float, float]] = {} # key -> (tokens, last_time)
        self._lock = asyncio.Lock()

    async def acquire_request(self, key: str) -> bool:
        async with self._lock:
            now = time.monotonic()
            if key not in self._buckets:
                self._buckets[key] = (self.burst - 1, now)
                return True

            tokens, last_time = self._buckets[key]
            elapsed = now - last_time
            # Replenish tokens based on RPS
            tokens = min(self.burst, tokens + elapsed * self.rps)
            
            if tokens >= 1.0:
                self._buckets[key] = (tokens - 1.0, now)
                return True
            else:
                retry_after = int((1.0 - tokens) / self.rps) + 1
                raise RateLimitExceededError(
                    message=f"Rate limit exceeded for {key}. Max RPS is {self.rps}.",
                    retry_after=retry_after
                )

    async def acquire_tokens(self, key: str, requested_tokens: int) -> bool:
        async with self._lock:
            now = time.monotonic()
            rate_per_sec = self.tpm / 60.0
            max_token_burst = self.tpm / 2.0

            if key not in self._token_buckets:
                self._token_buckets[key] = (max_token_burst - requested_tokens, now)
                return True

            tokens, last_time = self._token_buckets[key]
            elapsed = now - last_time
            tokens = min(max_token_burst, tokens + elapsed * rate_per_sec)

            if tokens >= requested_tokens:
                self._token_buckets[key] = (tokens - requested_tokens, now)
                return True
            else:
                retry_after = int((requested_tokens - tokens) / rate_per_sec) + 1
                raise RateLimitExceededError(
                    message=f"Token budget throughput exceeded for {key}. Max TPM is {self.tpm}.",
                    retry_after=retry_after
                )


global_rate_limiter = TokenBucketRateLimiter()
