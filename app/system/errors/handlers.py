from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.system.responses.api_response import fail


def register_error_handlers(app):
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content=fail(
                message=exc.detail if isinstance(exc.detail, str) else "HTTP Error",
                code=f"HTTP_{exc.status_code}",
            ),
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content=fail(
                message="Validation error",
                code="VALIDATION_ERROR",
                meta={"details": exc.errors()},
            ),
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content=fail(
                message="Internal server error",
                code="INTERNAL_ERROR",
            ),
        )
