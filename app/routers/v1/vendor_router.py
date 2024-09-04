from typing import Annotated

from fastapi import APIRouter, Depends, Path
from uuid import UUID

from gfmodules_python_shared.schema.pagination.page_schema import Page
from gfmodules_python_shared.schema.pagination.pagination_query_params_schema import PaginationQueryParams

from app.container import get_vendor_service
from app.db.services.vendor_service import VendorService
from app.schemas.vendor.schema import VendorDto

router = APIRouter(prefix="/vendors", tags=["vendors"])


@router.get("", summary="Get all vendors")
def get_paginated(
    query: Annotated[PaginationQueryParams, Depends()],
    vendor_service: VendorService = Depends(
        get_vendor_service
    ),
) -> Page[VendorDto]:
    return vendor_service.get_paginated(limit=query.limit, offset=query.offset)


@router.get("/{id}", summary="Get vendor by id")
def get(
        id_: UUID = Path(alias="id"),
        vendor_service: VendorService = Depends(
            get_vendor_service
        ),
) -> VendorDto:
    return vendor_service.get(id_)
