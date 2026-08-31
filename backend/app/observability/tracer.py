import uuid
import time
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field


class Span(BaseModel):
    span_id: str = Field(default_factory=lambda: uuid.uuid4().hex[:16])
    trace_id: str
    parent_span_id: Optional[str] = None
    name: str
    kind: str = "llm"
    start_time: float = Field(default_factory=time.time)
    end_time: Optional[float] = None
    duration_ms: Optional[float] = None
    status: str = "ok"
    attributes: Dict[str, Any] = Field(default_factory=dict)

    def finish(self, status: str = "ok") -> None:
        self.end_time = time.time()
        self.duration_ms = (self.end_time - self.start_time) * 1000
        self.status = status


class AtlasTracer:
    """OpenTelemetry-compatible trace and span manager for request waterfalls."""
    def __init__(self):
        self.spans: List[Span] = []

    def start_trace(self, name: str, trace_id: Optional[str] = None) -> Span:
        t_id = trace_id or uuid.uuid4().hex[:32]
        span = Span(trace_id=t_id, name=name)
        self.spans.append(span)
        return span

    def start_child_span(self, parent_span: Span, name: str, kind: str = "llm") -> Span:
        span = Span(trace_id=parent_span.trace_id, parent_span_id=parent_span.span_id, name=name, kind=kind)
        self.spans.append(span)
        return span


atlas_tracer = AtlasTracer()
