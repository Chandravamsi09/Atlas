from typing import Optional, AsyncGenerator
from fastapi import Depends, HTTPException, status, Header, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.core.config import settings
from backend.app.core.security import decode_access_token, hash_api_key
from backend.app.core.context import set_tenant_context, set_user_context, set_api_key_context
from backend.app.core.rbac import Role, Scope, role_has_permission
from backend.app.core.exceptions import AuthenticationError, AuthorizationError
from backend.app.db.session import get_async_db
from backend.app.models.user import User
from backend.app.models.organization import Organization, OrgMembership
from backend.app.models.api_key import APIKey

security = HTTPBearer(auto_error=False)


async def get_current_user_and_tenant(
    credentials: Optional[HTTPAuthorizationCredentials] = Security(security),
    x_api_key: Optional[str] = Header(None, alias="X-API-Key"),
    x_tenant_id: Optional[str] = Header(None, alias="X-Tenant-ID"),
    db: AsyncSession = Depends(get_async_db)
) -> tuple[Optional[User], str, Role]:
    """
    Authenticates requests via JWT Bearer Token OR Atlas API Key.
    Extracts and initializes contextvars for multi-tenant isolation.
    """
    if x_api_key:
        hashed = hash_api_key(x_api_key)
        stmt = select(APIKey).where(APIKey.hashed_key == hashed, APIKey.is_active == True)
        result = await db.execute(stmt)
        api_key_obj = result.scalar_one_or_none()
        if not api_key_obj:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or inactive API Key")
        
        set_tenant_context(api_key_obj.org_id)
        set_api_key_context(api_key_obj.id)
        return None, api_key_obj.org_id, Role.SERVICE_ACCOUNT

    if credentials and credentials.credentials:
        payload = decode_access_token(credentials.credentials)
        if not payload or "sub" not in payload:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        
        user_id = payload["sub"]
        user = await db.get(User, user_id)
        if not user or not user.is_active:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User inactive or deleted")

        org_id = x_tenant_id or payload.get("org_id")
        if not org_id:
            # Fallback to user's first organization
            stmt = select(OrgMembership).where(OrgMembership.user_id == user.id)
            res = await db.execute(stmt)
            membership = res.scalar_one_or_none()
            if membership:
                org_id = membership.org_id
                role = Role(membership.role)
            else:
                org_id = "default"
                role = Role.OWNER
        else:
            stmt = select(OrgMembership).where(OrgMembership.user_id == user.id, OrgMembership.org_id == org_id)
            res = await db.execute(stmt)
            membership = res.scalar_one_or_none()
            role = Role(membership.role) if membership else Role.VIEWER

        set_user_context(user.id)
        set_tenant_context(org_id)
        return user, org_id, role

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing Authentication Header (Bearer or X-API-Key)")


def require_permission(required_scope: Scope):
    def checker(auth_data = Depends(get_current_user_and_tenant)):
        user, org_id, role = auth_data
        if not role_has_permission(role, required_scope):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permission denied: Missing required scope '{required_scope.value}' for role '{role.value}'"
            )
        return auth_data
    return checker
