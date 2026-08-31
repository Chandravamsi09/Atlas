from typing import Dict, Any, List
from pydantic import BaseModel, Field


class AgentState(BaseModel):
    """State context passed between connected nodes in an execution DAG graph."""
    messages: List[Dict[str, Any]] = Field(default_factory=list)
    context_data: Dict[str, Any] = Field(default_factory=dict)
    current_step: int = 0
    total_tokens: int = 0
    errors: List[str] = Field(default_factory=list)
    hitl_pending: bool = False
    hitl_approved: bool = True
