import logging
import uuid
from typing import Sequence

from fastapi import APIRouter, Depends, Path

from app.container import get_role_database_service
from app.db.services.role_database_service import (
    RoleDatabaseServiceInterface,
)
from app.dto.RoleDto import RoleDto

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/roles", tags=["roles"])


@router.get("/", summary="Get all roles")
def get_all(
    role_database_service: RoleDatabaseServiceInterface = Depends(
        get_role_database_service
    ),
) -> Sequence[RoleDto]:
    return role_database_service.get_all()


@router.get("/{id}", summary="Get role by id")
def get(
    id_: uuid.UUID = Path(alias="id"),
    role_database_service: RoleDatabaseServiceInterface = Depends(
        get_role_database_service
    ),
) -> RoleDto:
    return role_database_service.get(id_=id_)
