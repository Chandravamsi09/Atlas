# Atlas Platform API v1 Reference

## Endpoints Overview

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/v1/chat/completions` | Unified multi-provider chat completion with smart routing |
| `GET`  | `/api/v1/healthz` | System health check and service status |
| `POST` | `/api/v1/prompts` | Create or update versioned prompt templates |
| `POST` | `/api/v1/workflows/execute` | Execute stateful agent DAG execution graph |
| `POST` | `/api/v1/knowledge/ingest` | Parse and chunk documents into hybrid vector stores |
| `GET`  | `/api/v1/traces` | Query OpenTelemetry spans and waterfall metrics |
