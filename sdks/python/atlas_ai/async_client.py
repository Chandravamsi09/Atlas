import httpx
from typing import Dict, Any, List, Optional


class AsyncAtlasClient:
    """Asynchronous Python client for Atlas AI Platform."""
    def __init__(self, api_key: str, base_url: str = "http://localhost:8000/api/v1"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {"X-API-Key": self.api_key, "Content-Type": "application/json"}

    async def chat_complete(self, model: str, messages: List[Dict[str, str]], **kwargs: Any) -> Dict[str, Any]:
        payload = {"model": model, "messages": messages, **kwargs}
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post(f"{self.base_url}/chat/completions", headers=self.headers, json=payload)
            resp.raise_for_status()
            return resp.json()
