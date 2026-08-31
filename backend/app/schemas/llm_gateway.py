from typing import List, Dict, Any, Optional, Union, Literal
from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: Literal["system", "user", "assistant", "tool", "function"]
    content: str
    name: Optional[str] = None
    tool_call_id: Optional[str] = None
    tool_calls: Optional[List[Dict[str, Any]]] = None


class ToolDefinition(BaseModel):
    type: Literal["function"] = "function"
    function: Dict[str, Any] # {name, description, parameters}


class ChatCompletionRequest(BaseModel):
    model: str = Field(..., description="Target model name or routing alias e.g. gpt-4o, claude-3-5-sonnet, fast, smart, cost-optimized")
    messages: List[ChatMessage]
    temperature: Optional[float] = Field(default=0.7, ge=0.0, le=2.0)
    top_p: Optional[float] = Field(default=1.0, ge=0.0, le=1.0)
    max_tokens: Optional[int] = Field(default=2048, ge=1)
    stream: Optional[bool] = False
    tools: Optional[List[ToolDefinition]] = None
    tool_choice: Optional[Union[str, Dict[str, Any]]] = None
    stop: Optional[Union[str, List[str]]] = None
    presence_penalty: Optional[float] = 0.0
    frequency_penalty: Optional[float] = 0.0
    user: Optional[str] = None
    
    # Atlas Extension Parameters
    routing_strategy: Optional[Literal["direct", "lowest_latency", "lowest_cost", "fallback_cascade", "round_robin"]] = "direct"
    enable_cache: Optional[bool] = True
    guardrails_enabled: Optional[bool] = True
    tags: Optional[List[str]] = Field(default_factory=list)


class UsageStats(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0
    cost_usd: float = 0.0
    latency_ms: float = 0.0
    cache_hit: bool = False


class ChatChoice(BaseModel):
    index: int = 0
    message: ChatMessage
    finish_reason: Optional[str] = "stop"


class ChatCompletionResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    provider: str
    choices: List[ChatChoice]
    usage: UsageStats
    cached: bool = False
    trace_id: Optional[str] = None


class ChatCompletionChunkChoice(BaseModel):
    index: int = 0
    delta: Dict[str, Any]
    finish_reason: Optional[str] = None


class ChatCompletionChunk(BaseModel):
    id: str
    object: str = "chat.completion.chunk"
    created: int
    model: str
    provider: str
    choices: List[ChatCompletionChunkChoice]
    usage: Optional[UsageStats] = None
