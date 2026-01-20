from typing import Any, Optional, Dict


def ok(data: Any = None, message: str = "OK", meta: Optional[Dict[str, Any]] = None):
    return {
        "success": True,
        "message": message,
        "data": data,
        "meta": meta or {},
    }


def fail(message: str = "Error", code: str = "ERROR", meta: Optional[Dict[str, Any]] = None):
    return {
        "success": False,
        "message": message,
        "error": {"code": code},
        "meta": meta or {},
    }
