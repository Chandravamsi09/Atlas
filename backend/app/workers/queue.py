import asyncio
from typing import Dict, Any, Callable, Awaitable, List


class InMemoryJobQueue:
    """Asynchronous background task runner for batch embeddings, evals, and rollups."""
    def __init__(self):
        self._queue: asyncio.Queue = asyncio.Queue()
        self._handlers: Dict[str, Callable[[Dict[str, Any]], Awaitable[None]]] = {}

    def register_handler(self, task_type: str, handler: Callable[[Dict[str, Any]], Awaitable[None]]) -> None:
        self._handlers[task_type] = handler

    async def enqueue(self, task_type: str, payload: Dict[str, Any]) -> None:
        await self._queue.put({"type": task_type, "payload": payload})

    async def process_one(self) -> None:
        if not self._queue.empty():
            item = await self._queue.get()
            t_type = item["type"]
            if t_type in self._handlers:
                await self._handlers[t_type](item["payload"])
            self._queue.task_done()


job_queue = InMemoryJobQueue()
