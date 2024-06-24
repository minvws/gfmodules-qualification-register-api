import logging
import uuid
from typing import Sequence

from fastapi import APIRouter, Depends, Path

from app.container import (
    get_system_type_database_service,
)
from app.db.services.system_type_database_service import (
    SystemTypeDatabaseServiceInterface,
)
from app.dto.SystemTypeDto import SystemTypeDto

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/system_types", tags=["system types"])


@router.get("/", summary="Get all system types")
def get_all(
    system_type_database_service: SystemTypeDatabaseServiceInterface = Depends(
        get_system_type_database_service
    ),
) -> Sequence[SystemTypeDto]:
    return system_type_database_service.get_all()


@router.get("/{id}", summary="Get system type by id")
def get(
    id_: uuid.UUID = Path(alias="id"),
    system_type_database_service: SystemTypeDatabaseServiceInterface = Depends(
        get_system_type_database_service
    ),
) -> SystemTypeDto:
    return system_type_database_service.get(id_)
