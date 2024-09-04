from typing import Annotated

from fastapi import APIRouter, Depends, Path
from uuid import UUID

from gfmodules_python_shared.schema.pagination.page_schema import Page
from gfmodules_python_shared.schema.pagination.pagination_query_params_schema import PaginationQueryParams

from app.container import get_system_type_service
from app.db.services.system_type_service import SystemTypeService
from app.schemas.system_type.schema import SystemTypeDto

router = APIRouter(prefix="/system-types", tags=["system types"])


@router.get("", summary="Get all system types")
def get_paginated(
    query: Annotated[PaginationQueryParams, Depends()],
    system_type_service: SystemTypeService = Depends(
        get_system_type_service
    ),
) -> Page[SystemTypeDto]:
    return system_type_service.get_paginated(limit=query.limit, offset=query.offset)


@router.get("/{id}", summary="Get system type by id")
def get(
    id_: UUID = Path(alias="id"),
    system_type_service: SystemTypeService = Depends(
        get_system_type_service
    ),
) -> SystemTypeDto:
    return system_type_service.get(id_)
