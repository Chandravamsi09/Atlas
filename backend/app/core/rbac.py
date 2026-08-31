from enum import Enum
from typing import Set, List, Dict


class Role(str, Enum):
    OWNER = "owner"
    ADMIN = "admin"
    ENGINEER = "engineer"
    ANALYST = "analyst"
    VIEWER = "viewer"
    SERVICE_ACCOUNT = "service_account"


class Scope(str, Enum):
    # Models & Gateway
    MODELS_READ = "models:read"
    MODELS_INVOKE = "models:invoke"
    
    # PromptOps
    PROMPTS_READ = "prompts:read"
    PROMPTS_WRITE = "prompts:write"
    PROMPTS_DELETE = "prompts:delete"
    PROMPTS_DEPLOY = "prompts:deploy"
    
    # Workflows & Agents
    WORKFLOWS_READ = "workflows:read"
    WORKFLOWS_WRITE = "workflows:write"
    WORKFLOWS_EXECUTE = "workflows:execute"
    
    # Knowledge & RAG
    KNOWLEDGE_READ = "knowledge:read"
    KNOWLEDGE_WRITE = "knowledge:write"
    KNOWLEDGE_DELETE = "knowledge:delete"
    
    # Guardrails
    GUARDRAILS_READ = "guardrails:read"
    GUARDRAILS_WRITE = "guardrails:write"
    
    # Evaluations & Benchmarks
    EVALUATIONS_READ = "evaluations:read"
    EVALUATIONS_RUN = "evaluations:run"
    
    # Observability & Traces
    TRACES_READ = "traces:read"
    METRICS_READ = "metrics:read"
    
    # Admin & IAM
    ORG_READ = "org:read"
    ORG_WRITE = "org:write"
    USERS_MANAGE = "users:manage"
    API_KEYS_MANAGE = "api_keys:manage"
    BILLING_MANAGE = "billing:manage"
    AUDIT_READ = "audit:read"


ROLE_PERMISSIONS: Dict[Role, Set[Scope]] = {
    Role.OWNER: set(Scope),
    Role.ADMIN: set(Scope) - {Scope.BILLING_MANAGE},
    Role.ENGINEER: {
        Scope.MODELS_READ, Scope.MODELS_INVOKE,
        Scope.PROMPTS_READ, Scope.PROMPTS_WRITE, Scope.PROMPTS_DEPLOY,
        Scope.WORKFLOWS_READ, Scope.WORKFLOWS_WRITE, Scope.WORKFLOWS_EXECUTE,
        Scope.KNOWLEDGE_READ, Scope.KNOWLEDGE_WRITE,
        Scope.GUARDRAILS_READ, Scope.GUARDRAILS_WRITE,
        Scope.EVALUATIONS_READ, Scope.EVALUATIONS_RUN,
        Scope.TRACES_READ, Scope.METRICS_READ,
        Scope.ORG_READ, Scope.API_KEYS_MANAGE,
    },
    Role.ANALYST: {
        Scope.MODELS_READ, Scope.MODELS_INVOKE,
        Scope.PROMPTS_READ, Scope.WORKFLOWS_READ, Scope.KNOWLEDGE_READ,
        Scope.GUARDRAILS_READ, Scope.EVALUATIONS_READ, Scope.EVALUATIONS_RUN,
        Scope.TRACES_READ, Scope.METRICS_READ, Scope.ORG_READ,
    },
    Role.VIEWER: {
        Scope.MODELS_READ, Scope.PROMPTS_READ, Scope.WORKFLOWS_READ,
        Scope.KNOWLEDGE_READ, Scope.GUARDRAILS_READ, Scope.EVALUATIONS_READ,
        Scope.TRACES_READ, Scope.METRICS_READ, Scope.ORG_READ,
    },
    Role.SERVICE_ACCOUNT: {
        Scope.MODELS_INVOKE, Scope.PROMPTS_READ, Scope.WORKFLOWS_EXECUTE,
        Scope.KNOWLEDGE_READ, Scope.TRACES_READ,
    }
}


def role_has_permission(role: Role, required_scope: Scope) -> bool:
    allowed_scopes = ROLE_PERMISSIONS.get(role, set())
    return required_scope in allowed_scopes


def check_scopes_allowed(role: Role, scopes: List[Scope]) -> bool:
    allowed = ROLE_PERMISSIONS.get(role, set())
    return all(s in allowed for s in scopes)
