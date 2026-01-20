import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


class RequestIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("x-request-id") or str(uuid.uuid4())

        # Attach for internal use
        request.state.request_id = request_id

        response = await call_next(request)

        # Return it back to caller
        response.headers["x-request-id"] = request_id
        return response
