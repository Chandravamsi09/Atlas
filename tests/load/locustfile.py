import random
from locust import HttpUser, task, between


class AtlasLoadTestUser(HttpUser):
    """Simulates high-concurrency enterprise traffic hitting Atlas Gateway."""
    wait_time = between(0.1, 0.5)

    @task(10)
    def test_health_check(self):
        self.client.get("/api/v1/healthz")

    @task(5)
    def test_chat_completion_mock(self):
        headers = {"X-API-Key": "atl_live_load_test_key_sample", "Content-Type": "application/json"}
        payload = {
            "model": "mock-gpt-4o",
            "messages": [
                {"role": "system", "content": "You are a fast enterprise assistant."},
                {"role": "user", "content": f"Load test query session ID {random.randint(1000, 9999)}"}
            ],
            "temperature": 0.5,
            "max_tokens": 128
        }
        self.client.post("/api/v1/chat/completions", json=payload, headers=headers)
