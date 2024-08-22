import logging
from typing import Annotated

from fastapi import APIRouter, Depends
from gfmodules_python_shared.schema.pagination.page_schema import Page
from gfmodules_python_shared.schema.pagination.pagination_query_params_schema import (
    PaginationQueryParams,
)

from app.container import (
    get_healthcare_provider_service,
    get_vendor_qualification_service,
)
from app.db.services.healthcare_provider_service import HealthcareProviderService
from app.db.services.vendor_qualification_service import VendorQualificationService
from app.openapi.responses import api_version_header_responses
from app.schemas.healthcare_provider_qualification.schema import (
    QualifiedHealthcareProviderDTO,
)
from app.schemas.qualification.schema import QualificationDto
from app.schemas.vendor_qualifications.schema import QualifiedVendorDTO

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/qualifications", tags=["qualifications"])


@router.get(
    "",
    summary="Get all qualifications based on the supplied query params",
    responses={**api_version_header_responses([200])},
)
def get_paginated(
    query: Annotated[PaginationQueryParams, Depends()],
    healthcare_provider_service: HealthcareProviderService = Depends(
        get_healthcare_provider_service
    ),
) -> Page[QualificationDto]:
    return healthcare_provider_service.get_paginated(
        limit=query.limit, offset=query.offset
    )


@router.get(
    "/vendors",
    summary="Get all qualifications for software vendors",
    responses={**api_version_header_responses([200])},
)
def get_vendor_qualifications(
    query: Annotated[PaginationQueryParams, Depends()],
    service: VendorQualificationService = Depends(get_vendor_qualification_service),
) -> Page[QualifiedVendorDTO]:
    return service.get_paginated(limit=query.limit, offset=query.offset)


@router.get(
    "/healthcare-providers",
    summary="Get paginated qualifications for healthcare providers",
    responses={**api_version_header_responses([200])},
)
def get_healthcare_provider_qualifications(
    query: Annotated[PaginationQueryParams, Depends()],
    service: HealthcareProviderService = Depends(get_healthcare_provider_service),
) -> Page[QualifiedHealthcareProviderDTO]:
    return service.get_qualified_healthcare_providers(
        limit=query.limit, offset=query.offset
    )
