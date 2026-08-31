import sys
import io
import contextlib
from typing import Dict, Any
from backend.app.agents.tools.base import BaseTool


class PythonCodeSandboxTool(BaseTool):
    """Sandboxed in-process Python execution environment for analytical compute."""
    
    def __init__(self):
        super().__init__(
            name="python_code_sandbox",
            description="Execute safe computational Python scripts, calculations, or data transformations.",
            parameters_schema={
                "type": "object",
                "properties": {"code": {"type": "string", "description": "Python executable code block"}},
                "required": ["code"]
            }
        )

    async def run(self, code: str) -> Dict[str, Any]:
        stdout_buf = io.StringIO()
        stderr_buf = io.StringIO()
        safe_globals = {"__builtins__": {"print": print, "range": range, "len": len, "sum": sum, "min": min, "max": max}}
        
        try:
            with contextlib.redirect_stdout(stdout_buf), contextlib.redirect_stderr(stderr_buf):
                exec(code, safe_globals)
            return {
                "success": True,
                "stdout": stdout_buf.getvalue(),
                "stderr": stderr_buf.getvalue()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "stderr": stderr_buf.getvalue()
            }
