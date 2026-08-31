import time
from typing import Dict
from backend.app.core.exceptions import ProviderCircuitBreakerOpenError


class CircuitBreaker:
    """
    Failsafe circuit breaker with Closed, Open, and Half-Open states.
    Prevents cascading downstream LLM provider outages.
    """
    def __init__(self, failure_threshold: int = 5, recovery_timeout_sec: float = 30.0):
        self.failure_threshold = failure_threshold
        self.recovery_timeout_sec = recovery_timeout_sec
        self.failure_counts: Dict[str, int] = {}
        self.last_failure_times: Dict[str, float] = {}
        self.states: Dict[str, str] = {} # "closed", "open", "half-open"

    def record_success(self, provider: str) -> None:
        self.failure_counts[provider] = 0
        self.states[provider] = "closed"

    def record_failure(self, provider: str) -> None:
        now = time.monotonic()
        count = self.failure_counts.get(provider, 0) + 1
        self.failure_counts[provider] = count
        self.last_failure_times[provider] = now

        if count >= self.failure_threshold:
            self.states[provider] = "open"

    def check_state(self, provider: str) -> None:
        state = self.states.get(provider, "closed")
        if state == "open":
            last_fail = self.last_failure_times.get(provider, 0)
            if (time.monotonic() - last_fail) > self.recovery_timeout_sec:
                self.states[provider] = "half-open"
                return
            raise ProviderCircuitBreakerOpenError(
                f"Circuit breaker is OPEN for provider [{provider}]. Outage mitigation active."
            )


circuit_breaker = CircuitBreaker()
