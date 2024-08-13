import uuid
from typing import List

from fastapi import APIRouter, Depends, Path

from app.container import get_role_service
from app.db.services.role_service import RoleService
from app.openapi.responses import api_version_header_responses
from app.schemas.roles.schema import RoleDto

router = APIRouter(prefix="/roles", tags=["roles"])


@router.get("", summary="Get all roles", responses={**api_version_header_responses([200])})
def get_all(
    role_service: RoleService = Depends(
        get_role_service
    ),
) -> List[RoleDto]:
    return role_service.get_all()


@router.get("/{id}", summary="Get role by id", responses={**api_version_header_responses([200, 404, 422])})
def get(
    id_: uuid.UUID = Path(alias="id"),
    role_service: RoleService = Depends(
        get_role_service
    ),
) -> RoleDto:
    return role_service.get(id_=id_)
