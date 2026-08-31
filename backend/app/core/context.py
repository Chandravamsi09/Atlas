import contextvars
from typing import Optional, Dict, Any

_tenant_id_ctx: contextvars.ContextVar[Optional[str]] = contextvars.ContextVar("tenant_id", default=None)
_user_id_ctx: contextvars.ContextVar[Optional[str]] = contextvars.ContextVar("user_id", default=None)
_request_id_ctx: contextvars.ContextVar[Optional[str]] = contextvars.ContextVar("request_id", default=None)
_api_key_id_ctx: contextvars.ContextVar[Optional[str]] = contextvars.ContextVar("api_key_id", default=None)


def set_tenant_context(tenant_id: str) -> None:
    _tenant_id_ctx.set(tenant_id)


def get_tenant_context() -> Optional[str]:
    return _tenant_id_ctx.get()


def set_user_context(user_id: str) -> None:
    _user_id_ctx.set(user_id)


def get_user_context() -> Optional[str]:
    return _user_id_ctx.get()


def set_request_id_context(request_id: str) -> None:
    _request_id_ctx.set(request_id)


def get_request_id_context() -> Optional[str]:
    return _request_id_ctx.get()


def set_api_key_context(api_key_id: str) -> None:
    _api_key_id_ctx.set(api_key_id)


def get_api_key_context() -> Optional[str]:
    return _api_key_id_ctx.get()
