from typing import Annotated

from fastapi import APIRouter, Depends, Path
from uuid import UUID

from gfmodules_python_shared.schema.pagination.page_schema import Page
from gfmodules_python_shared.schema.pagination.pagination_query_params_schema import PaginationQueryParams

from app.container import get_role_service
from app.db.services.role_service import RoleService
from app.openapi.responses import api_version_header_responses
from app.schemas.roles.schema import RoleDto

router = APIRouter(prefix="/roles", tags=["roles"])


@router.get("", summary="Get all roles", responses={**api_version_header_responses([200])})
def get_paginated(
    query: Annotated[PaginationQueryParams, Depends()],
    role_service: RoleService = Depends(
        get_role_service
    ),
) -> Page[RoleDto]:
    return role_service.get_paginated(limit=query.limit, offset=query.offset)


@router.get("/{id}", summary="Get role by id", responses={**api_version_header_responses([200, 404, 422])})
def get(
    id_: UUID = Path(alias="id"),
    role_service: RoleService = Depends(
        get_role_service
    ),
) -> RoleDto:
    return role_service.get(id_=id_)
