import logging
import sys
import json
from datetime import datetime
from typing import Any, Dict
from backend.app.core.context import get_tenant_context, get_request_id_context


class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_obj: Dict[str, Any] = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        tenant_id = get_tenant_context()
        if tenant_id:
            log_obj["tenant_id"] = tenant_id
        request_id = get_request_id_context()
        if request_id:
            log_obj["request_id"] = request_id

        if record.exc_info:
            log_obj["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_obj)


def setup_logging(debug: bool = False) -> logging.Logger:
    logger = logging.getLogger("atlas")
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    logger.handlers.clear()

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JSONFormatter())
    logger.addHandler(handler)
    return logger


logger = setup_logging()
