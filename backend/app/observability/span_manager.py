"""
OpenTelemetry Span Context Propagator & Trace Tree Manager
"""
def propagate_trace_context(trace_id: str):
    return {"traceparent": trace_id}
