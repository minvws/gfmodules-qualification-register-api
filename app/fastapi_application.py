import logging

from typing import Any

from fastapi import FastAPI
import uvicorn

from app.fastapi.setup import setup_fastapi, setup_fastapi_for_api, fastapi_mount_api
from app.routers.default_router import router as default_router
from app.routers.health_router import router as health_router
from app.routers.v1.qualification_router import router as qualification_router
from app.routers.v1.application_router import router as application_router
from app.routers.v1.role_router import router as role_router
from app.routers.v1.system_type_router import router as system_type_router
from app.routers.v1.vendor_router import router as vendor_router

from app.config import get_config


def get_uvicorn_params() -> dict[str, Any]:
    config = get_config()

    kwargs = {
        "host": config.uvicorn.host,
        "port": config.uvicorn.port,
        "reload": config.uvicorn.reload,
    }
    if config.uvicorn.use_ssl:
        if (
            config.uvicorn.ssl_base_dir
            and config.uvicorn.ssl_cert_file
            and config.uvicorn.ssl_key_file
        ):
            kwargs["ssl_keyfile"] = (
                config.uvicorn.ssl_base_dir + "/" + config.uvicorn.ssl_key_file
            )
            kwargs["ssl_certfile"] = (
                config.uvicorn.ssl_base_dir + "/" + config.uvicorn.ssl_cert_file
            )

    return kwargs


def run() -> None:
    uvicorn.run("app.fastapi_application:create_fastapi_app", **get_uvicorn_params())


def create_fastapi_app() -> FastAPI:
    application_init()

    config = get_config()

    fastapi = setup_fastapi(config, [
        default_router,
        health_router,
    ])

    # v1 api
    fastapi_v1 = setup_fastapi_for_api(config, routers=[
        application_router,
        qualification_router,
        role_router,
        system_type_router,
        vendor_router,
    ], api_version="1.0.0")
    fastapi_mount_api(root_fastapi=fastapi, mount_path="/v1", api=fastapi_v1)

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