import logging

from typing import Any

from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from routers.default_router import router as default_router
from routers.health_router import router as health_router
from routers.qualification_router import router as qualification_router
from routers.application_router import router as application_router
from routers.role_router import router as role_router
from routers.system_type_router import router as system_type_router
from routers.vendor_router import router as vendor_router

from config import get_config


def get_uvicorn_params() -> dict[str, Any]:
    config = get_config()

    kwargs = {
        "host": config.uvicorn.host,
        "port": config.uvicorn.port,
        "reload": config.uvicorn.reload,
    }
    if config.uvicorn.use_ssl:
        kwargs["ssl_keyfile"] = (
            config.uvicorn.ssl_base_dir + "/" + config.uvicorn.ssl_key_file
        )
        kwargs["ssl_certfile"] = (
            config.uvicorn.ssl_base_dir + "/" + config.uvicorn.ssl_cert_file
        )
    return kwargs


def run() -> None:
    uvicorn.run("application:create_fastapi_app", **get_uvicorn_params())


def create_fastapi_app() -> FastAPI:
    application_init()
    fastapi = setup_fastapi()

    return fastapi


def application_init() -> None:
    setup_logging()


def setup_logging() -> None:
    loglevel = logging.getLevelName(get_config().app.loglevel.upper())

    if isinstance(loglevel, str):
        raise ValueError(f"Invalid loglevel {loglevel.upper()}")
    logging.basicConfig(
        level=loglevel,
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )


def setup_fastapi() -> FastAPI:
    config = get_config()

    fastapi = (
        FastAPI(docs_url=config.uvicorn.docs_url, redoc_url=config.uvicorn.redoc_url)
        if config.uvicorn.swagger_enabled
        else FastAPI(docs_url=None, redoc_url=None)
    )
    fastapi.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    routers = [
        default_router,
        health_router,
        qualification_router,
        application_router,
        role_router,
        system_type_router,
        vendor_router,
    ]
    for router in routers:
        fastapi.include_router(router)

    return fastapi
