from typing import List, Dict, Any, Optional

from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from app.config import Config
from app.middleware.api_version import ApiVersionHeaderMiddleware


def setup_fastapi(
        config: Config,
        routers: List[APIRouter],
        description: str = "",
        openapi_tags: Optional[List[Dict[str, Any]]] = None,
) -> FastAPI:
    title = "Qualification Register API"

    fastapi = (
        FastAPI(title=title, docs_url=config.uvicorn.docs_url, redoc_url=config.uvicorn.redoc_url, redirect_slashes=False, description=description, openapi_tags=openapi_tags)
        if config.uvicorn.swagger_enabled
        else FastAPI(title=title, docs_url=None, redoc_url=None, redirect_slashes=False, description=description, openapi_tags=openapi_tags)
    )

    fastapi.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    for router in routers:
        fastapi.include_router(router)

    return fastapi


def setup_fastapi_for_api(
        config: Config,
        routers: List[APIRouter],
        api_version: str,
        description: str = "",
        openapi_tags: Optional[List[Dict[str, Any]]] = None,
) -> FastAPI:
    fastapi = setup_fastapi(
        config,
        routers,
        description,
        openapi_tags
    )

    fastapi.add_middleware(ApiVersionHeaderMiddleware, api_version=api_version)

    return fastapi


def fastapi_mount_api(root_fastapi: FastAPI, mount_path: str, api: FastAPI) -> None:
    root_fastapi.mount(mount_path, api)

    @root_fastapi.get(mount_path, include_in_schema=False)
    async def docs_redirect() -> RedirectResponse:
        return RedirectResponse(url=mount_path + '/docs')
