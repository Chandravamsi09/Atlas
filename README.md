# Atlas Enterprise AI Platform & LLMOps Engine

**Atlas** is an enterprise-grade, distributed, multi-tenant AI Platform and LLMOps Orchestration Engine designed for high-throughput model serving, prompt lifecycle management (PromptOps), stateful agentic workflows (DAGs), hybrid retrieval-augmented generation (RAG), real-time safety guardrails, continuous evaluation (LLM-as-a-Judge & RAG Triad), and OpenTelemetry observability.

---

## Dependencies

- **Python**: `>=3.11` (Python 3.11, 3.12, 3.13, 3.14)
- **Node.js**: `>=18.0.0` (Node 20+ LTS recommended)
- **Database**: PostgreSQL 16+ with `pgvector` extension
- **Cache & Message Broker**: Redis 7.2+
- **Containerization**: Docker & Docker Compose v2.20+

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Chandravamsi09/Atlas.git
cd Atlas
```

### 2. Set Up Python Virtual Environment & Dependencies
```bash
python -m venv venv
# On Linux/macOS:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate

# Install Python requirements and package in editable mode
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .[dev]
```

### 3. Install Frontend Dependencies
```bash
cd frontend
npm install
cd ..
```

---

## Build

### 1. Build the Frontend Production Bundle
```bash
cd frontend
npm run build
cd ..
```

### 2. Build Container Images with Docker
```bash
# Build the unified backend container
docker build -t atlas-backend -f Dockerfile .

# Or build the complete production multi-container stack
docker-compose -f deploy/docker-compose.yml build
```

---

## Run

### Option A: Running with Docker Compose (Recommended)
```bash
# Start all infrastructure services (Postgres + pgvector, Redis, FastAPI Gateway, Next.js Web UI)
docker-compose -f deploy/docker-compose.yml up -d
```

### Option B: Running Locally for Development

1. **Start Backend API Gateway**:
```bash
uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload
```

2. **Start Frontend Developer Portal**:
```bash
cd frontend
npm run dev
```

The services will be accessible at:
- **Web UI & Developer Portal**: [http://localhost:3000](http://localhost:3000)
- **FastAPI Interactive Swagger Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **API Health Check**: [http://localhost:8000/api/v1/healthz](http://localhost:8000/api/v1/healthz)

---

## Usage

### 1. Seed Tenant Credentials
```bash
python scripts/seed_data.py
```

### 2. Execute Unified LLM Chat Completion (Python SDK)
```python
from sdks.python.atlas_ai.client import AtlasClient

client = AtlasClient(api_key="atl_live_sample_key", base_url="http://localhost:8000/api/v1")
response = client.chat_complete(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are an enterprise AI assistant."},
        {"role": "user", "content": "Analyze quarterly EBITDA margins."}
    ],
    temperature=0.7
)
print(response)
```

### 3. Run Automated Test Suites
```bash
# Execute unit, security, and evaluation tests
pytest tests/unit/ tests/security/ tests/evaluation/ -v
```

---

## License

Proprietary and Confidential. Copyright (c) 2026 Atlas AI Inc. All Rights Reserved.
