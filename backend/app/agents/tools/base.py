import abc
from typing import Dict, Any, Optional


class BaseTool(abc.ABC):
    """Abstract base class for sandboxed agent tools."""
    def __init__(self, name: str, description: str, parameters_schema: Dict[str, Any]):
        self.name = name
        self.description = description
        self.parameters_schema = parameters_schema

    @abc.abstractmethod
    async def run(self, **kwargs: Any) -> Dict[str, Any]:
        pass
