from fastapi import APIRouter
from backend.app.api.v1.endpoints import (
    auth,
    health,
    chat,
    metrics,
    traces,
    prompts,
    workflows,
    knowledge_bases,
    guardrails,
    evaluations,
    api_keys,
    organizations,
    users
)

api_router = APIRouter()

# Core Authentication & Health
api_router.include_router(auth.router)
api_router.include_router(health.router)

# Model Gateway & Inference
api_router.include_router(chat.router)
api_router.include_router(metrics.router)
api_router.include_router(traces.router)

# Enterprise LLMOps Lifecycle
api_router.include_router(prompts.router, prefix="/prompts", tags=["PromptOps"])
api_router.include_router(workflows.router, prefix="/workflows", tags=["Agent Workflows"])
api_router.include_router(knowledge_bases.router, prefix="/knowledge-bases", tags=["RAG"])
api_router.include_router(guardrails.router, prefix="/guardrails", tags=["Guardrails & Safety"])
api_router.include_router(evaluations.router, prefix="/evaluations", tags=["Evaluations"])
api_router.include_router(api_keys.router, prefix="/api-keys", tags=["API Keys"])
api_router.include_router(organizations.router, prefix="/organizations", tags=["Organizations"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
