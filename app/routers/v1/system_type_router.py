import uuid
from typing import Sequence

from fastapi import APIRouter, Depends, Path

from app.container import (
    get_system_type_database_service,
)
from app.db.services.system_type_database_service import (
    SystemTypeDatabaseServiceInterface,
)
from app.openapi.responses import api_version_header_responses
from app.schemas.system_type.schema import SystemTypeDto

router = APIRouter(prefix="/system-types", tags=["system types"])


@router.get("", summary="Get all system types", responses={**api_version_header_responses([200])})
def get_all(
    system_type_database_service: SystemTypeDatabaseServiceInterface = Depends(
        get_system_type_database_service
    ),
) -> Sequence[SystemTypeDto]:
    return system_type_database_service.get_all()


@router.get("/{id}", summary="Get system type by id", responses={**api_version_header_responses([200, 404, 422])})
def get(
    id_: uuid.UUID = Path(alias="id"),
    system_type_database_service: SystemTypeDatabaseServiceInterface = Depends(
        get_system_type_database_service
    ),
) -> SystemTypeDto:
    return system_type_database_service.get(id_)
