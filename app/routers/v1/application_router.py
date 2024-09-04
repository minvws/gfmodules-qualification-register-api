import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Path
from uuid import UUID

from gfmodules_python_shared.schema.pagination.page_schema import Page
from gfmodules_python_shared.schema.pagination.pagination_query_params_schema import PaginationQueryParams

from app.container import get_application_service
from app.db.services.application_service import ApplicationService
from app.schemas.application.schema import ApplicationWithVendorDto

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/applications", tags=["applications"])


@router.get("", summary="Get all applications")
def get_paginated(
    query: Annotated[PaginationQueryParams, Depends()],
    application_service: ApplicationService = Depends(
        get_application_service
    ),
) -> Page[ApplicationWithVendorDto]:
    return application_service.get_paginated(limit=query.limit, offset=query.offset)


@router.get("/{id}", summary="Get application by id")
def get(
    id_: UUID = Path(alias="id"),
    application_service: ApplicationService = Depends(
        get_application_service
    ),
) -> ApplicationWithVendorDto:
    return application_service.get(id_)
