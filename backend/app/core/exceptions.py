from typing import Any, Dict, Optional
from fastapi import HTTPException, status


class AtlasException(Exception):
    """Base exception for all domain errors within Atlas Platform."""
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}


class AuthenticationError(AtlasException):
    """Raised when authentication fails or credentials are invalid."""
    pass


class AuthorizationError(AtlasException):
    """Raised when user or token lacks sufficient permissions/scopes."""
    pass


class RateLimitExceededError(AtlasException):
    """Raised when tenant token or request quota is exceeded."""
    def __init__(self, message: str = "Rate limit quota exceeded", retry_after: int = 60):
        super().__init__(message, {"retry_after": retry_after})
        self.retry_after = retry_after


class BudgetExceededError(AtlasException):
    """Raised when monthly financial or token budget has been exhausted."""
    pass


class ProviderAPIError(AtlasException):
    """Raised when downstream LLM provider returns non-200 response."""
    def __init__(self, provider: str, status_code: int, message: str, raw_response: Optional[str] = None):
        super().__init__(f"Provider [{provider}] failed with status {status_code}: {message}", {
            "provider": provider,
            "status_code": status_code,
            "raw_response": raw_response
        })
        self.provider = provider
        self.status_code = status_code


class ProviderCircuitBreakerOpenError(AtlasException):
    """Raised when circuit breaker is active due to repeated provider failures."""
    pass


class PromptTemplateError(AtlasException):
    """Raised when prompt Jinja2 compilation or variable substitution fails."""
    pass


class GuardrailViolationError(AtlasException):
    """Raised when input/output fails security, PII, or toxicity policies."""
    def __init__(self, rule_name: str, message: str, violation_type: str):
        super().__init__(message, {"rule_name": rule_name, "violation_type": violation_type})
        self.rule_name = rule_name
        self.violation_type = violation_type


class WorkflowExecutionError(AtlasException):
    """Raised when stateful agent DAG execution fails."""
    pass


class VectorIndexError(AtlasException):
    """Raised when vector search, indexing or embedding generation fails."""
    pass


def atlas_exception_to_http(exc: AtlasException) -> HTTPException:
    if isinstance(exc, AuthenticationError):
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=exc.message)
    elif isinstance(exc, AuthorizationError):
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=exc.message)
    elif isinstance(exc, RateLimitExceededError):
        return HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=exc.message,
            headers={"Retry-After": str(exc.retry_after)}
        )
    elif isinstance(exc, BudgetExceededError):
        return HTTPException(status_code=status.HTTP_402_PAYMENT_REQUIRED, detail=exc.message)
    elif isinstance(exc, GuardrailViolationError):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"error": "GuardrailViolation", "message": exc.message, "details": exc.details})
    elif isinstance(exc, ProviderCircuitBreakerOpenError):
        return HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=exc.message)
    elif isinstance(exc, ProviderAPIError):
        return HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=exc.message)
    return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=exc.message)
