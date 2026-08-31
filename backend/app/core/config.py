import os
from typing import List, Dict, Any, Optional
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Atlas AI Platform"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = Field(default="development", description="Environment: development, staging, production")
    DEBUG: bool = Field(default=False)
    SECRET_KEY: str = Field(default="atlas-super-secret-jwt-signing-key-32-chars-min-prod", description="JWT secret key")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # 7 days
    ALGORITHM: str = "HS256"

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
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    VERTEX_AI_PROJECT_ID: Optional[str] = None
    VERTEX_AI_LOCATION: str = "us-central1"
    AZURE_OPENAI_ENDPOINT: Optional[str] = None
    AZURE_OPENAI_API_KEY: Optional[str] = None
    GROQ_API_KEY: Optional[str] = None
    MISTRAL_API_KEY: Optional[str] = None
    VLLM_BASE_URL: Optional[str] = "http://localhost:8000/v1"
    OLLAMA_BASE_URL: Optional[str] = "http://localhost:11434"

    # Telemetry & Observability
    OTEL_EXPORTER_OTLP_ENDPOINT: Optional[str] = "http://localhost:4317"
    OTEL_SERVICE_NAME: str = "atlas-backend-gateway"
    ENABLE_METRICS: bool = True
    ENABLE_TRACING: bool = True

    # CORS Origins
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: Any) -> List[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        return []


settings = Settings()
