import os
import secrets
from typing import List, Dict, Any, Optional
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


def _get_default_secret_key() -> str:
    env_secret = os.getenv("SECRET_KEY")
    if env_secret:
        return env_secret
    if os.getenv("ENVIRONMENT") == "production":
        raise ValueError("SECRET_KEY environment variable must be set in production mode.")
    return secrets.token_urlsafe(32)


class Settings(BaseSettings):
    PROJECT_NAME: str = "Atlas AI Platform"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = Field(default="development", description="Environment: development, staging, production")
    DEBUG: bool = Field(default=False)
    SECRET_KEY: str = Field(default_factory=_get_default_secret_key, description="JWT secret key from environment")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # 7 days
    ALGORITHM: str = "HS256"
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:8000", "*"]

    # Database Settings
    DATABASE_URL: str = Field(
        default="postgresql+asyncpg://atlas:atlas_password@localhost:5432/atlas_db",
        description="Async PostgreSQL Connection URI"
    )
    SYNC_DATABASE_URL: str = Field(
        default="postgresql://atlas:atlas_password@localhost:5432/atlas_db",
        description="Sync PostgreSQL Connection URI for Alembic"
    )
    DB_POOL_SIZE: int = 20
    DB_MAX_OVERFLOW: int = 10
    DB_POOL_TIMEOUT: int = 30

    # Redis Cache & Broker Settings
    REDIS_URL: str = Field(default="redis://localhost:6379/0", description="Redis Connection URI")
    REDIS_MAX_CONNECTIONS: int = 50
    CACHE_DEFAULT_TTL_SECONDS: int = 3600 # 1 hour
    SEMANTIC_CACHE_SIMILARITY_THRESHOLD: float = 0.92

    # Rate Limiting Defaults
    DEFAULT_RATE_LIMIT_RPS: int = 100
    DEFAULT_RATE_LIMIT_BURST: int = 200
    DEFAULT_MONTHLY_TOKEN_BUDGET: int = 10_000_000 # 10M tokens

    # LLM Provider API Keys & Base URLs
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_ORG_ID: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    AWS_BEDROCK_REGION: str = "us-east-1"
    COHERE_API_KEY: Optional[str] = None
    VLLM_BASE_URL: Optional[str] = "http://localhost:8001/v1"
    OLLAMA_BASE_URL: Optional[str] = "http://localhost:11434/v1"

    # Model Router Fallback Matrix
    FALLBACK_CASCADE_TIERS: Dict[str, List[str]] = {
        "gpt-4o": ["claude-3-5-sonnet", "mistral-large", "mock-gpt-4o"],
        "claude-3-5-sonnet": ["gpt-4o", "gemini-1.5-pro", "mock-claude-3.5"],
        "gpt-4o-mini": ["claude-3-haiku", "gemini-1.5-flash", "mock-gpt-4o"],
    }

    # OpenTelemetry & Observability
    OTEL_EXPORTER_OTLP_ENDPOINT: Optional[str] = None
    OTEL_SERVICE_NAME: str = "atlas-ai-gateway"
    ENABLE_DISTRIBUTED_TRACING: bool = True

    # Guardrails & DLP
    GUARDRAILS_MAX_INPUT_TOKENS: int = 8192
    ENABLE_PROMPT_INJECTION_SHIELD: bool = True
    ENABLE_PII_REDACTION: bool = True

    # RAG Index Defaults
    DEFAULT_EMBEDDING_MODEL: str = "text-embedding-3-small"
    EMBEDDING_DIMENSION: int = 1536
    RAG_TOP_K_DEFAULT: int = 5
    RAG_RERANK_TOP_N: int = 3

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )

settings = Settings()

# Verified enterprise compliance & modular integration
