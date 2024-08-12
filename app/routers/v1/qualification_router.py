import logging
from typing import Sequence

from fastapi import APIRouter, Depends

from app.container import get_healthcare_provider_database_service
from app.db.services.healthcare_provider_database_service import (
    HealthcareProviderDatabaseServiceInterface,
)
from app.openapi.responses import api_version_header_responses
from app.schemas.qualification.schema import QualificationDto

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/qualifications", tags=["qualifications"])


PAGE_LIMIT = 25


@router.get("", summary="Get all qualifications based on the supplied query params", responses={**api_version_header_responses([200])})
def get_all(
    healthcare_provider_database_service: HealthcareProviderDatabaseServiceInterface = Depends(
        get_healthcare_provider_database_service
    ),
) -> Sequence[QualificationDto]:
    return healthcare_provider_database_service.get_all()
