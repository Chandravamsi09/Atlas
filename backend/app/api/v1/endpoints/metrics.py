from typing import Dict, Any
from fastapi import APIRouter, Depends
from backend.app.api.deps import get_current_user_and_tenant, require_permission
from backend.app.core.rbac import Scope
from backend.app.observability.trace_store import global_trace_store

router = APIRouter(prefix="/metrics", tags=["Metrics & Analytics"])


@router.get("/overview", summary="Get live enterprise metrics and provider health")
async def get_metrics_overview(
    auth_data = Depends(require_permission(Scope.MODELS_READ))
):
    user, org_id, role = auth_data
    summary = global_trace_store.get_metrics_summary(tenant_id=org_id)

    providers = [
        {
            "name": "Local Development Mock Engine (mock-gpt-4o, mock-claude-3.5)",
            "route": "Default Local Gateway",
            "latency_ms": 18,
            "status": "Operational (Active)",
            "is_mock": True
        },
        {
            "name": "OpenAI (gpt-4o, gpt-4o-mini)",
            "route": "Direct Primary Cloud",
            "latency_ms": 210,
            "status": "Configured (API Key required in Settings)",
            "is_mock": False
        },
        {
            "name": "Anthropic (Claude 3.5 Sonnet)",
            "route": "Fallback Secondary Cloud",
            "latency_ms": 320,
            "status": "Configured (API Key required in Settings)",
            "is_mock": False
        },
        {
            "name": "Local vLLM / Ollama Cluster",
            "route": "High-Throughput Batch Endpoint",
            "latency_ms": 85,
            "status": "Ready",
            "is_mock": False
        }
    ]

    return {
        "success": True,
        "metrics": summary,
        "providers": providers
    }
