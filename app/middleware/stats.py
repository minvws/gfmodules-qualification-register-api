import time
from typing import Callable, Awaitable

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

from app.stats import get_stats


class StatsdMiddleware(BaseHTTPMiddleware):
    """
    Middleware to record request info and response time for each request
    """
    def __init__(self, app: ASGIApp, module_name: str):
        super().__init__(app)
        self.module_name = module_name

    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        key = f"{self.module_name}.http.request.{request.method.lower()}.{request.url.path}"
        get_stats().inc(key)

        start_time = time.monotonic()
        response = await call_next(request)
        end_time = time.monotonic()

        response_time = int((end_time - start_time) * 1000)
        get_stats().timing(f"{self.module_name}.http.response_time", response_time)

        return response