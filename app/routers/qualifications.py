import logging
from typing import Sequence

from fastapi import APIRouter, Depends

from app.container import get_healthcare_provider_database_service
from app.db.services.healthcare_provider_database_service import HealthcareProviderDatabaseService
from app.dto.HealthcareProviderDto import HealthcareProviderDto

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/qualifications", tags=["qualifications"])


PAGE_LIMIT = 25


@router.get("/",
            summary="Get all qualifications based on the supplied query params")
def get_all(
        healthcare_provider_database_service: HealthcareProviderDatabaseService = Depends(get_healthcare_provider_database_service)
) -> Sequence[HealthcareProviderDto]:
    return healthcare_provider_database_service.get_all()
