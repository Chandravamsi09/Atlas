from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Depends, Query
from backend.app.api.deps import get_current_user_and_tenant, require_permission
from backend.app.core.rbac import Scope
from backend.app.observability.trace_store import global_trace_store

router = APIRouter(prefix="/traces", tags=["Observability & Traces"])


@router.get("/", summary="List live distributed traces")
async def list_traces(
    limit: int = Query(50, ge=1, le=100),
    auth_data = Depends(require_permission(Scope.MODELS_READ))
):
    user, org_id, role = auth_data
    traces = global_trace_store.get_traces(limit=limit, tenant_id=org_id)
    return {
        "success": True,
        "total": len(traces),
        "traces": traces
    }


@router.get("/{trace_id}", summary="Get specific trace span details")
async def get_trace_detail(
    trace_id: str,
    auth_data = Depends(require_permission(Scope.MODELS_READ))
):
    user, org_id, role = auth_data
    traces = global_trace_store.get_traces(100, tenant_id=org_id)
    for t in traces:
        if t["id"] == trace_id or t["trace_id"] == trace_id:
            return {"success": True, "trace": t}
    return {"success": False, "message": "Trace not found"}
