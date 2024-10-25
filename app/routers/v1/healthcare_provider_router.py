from fastapi import APIRouter, Depends, Path
from uuid import UUID

from app.container import get_healthcare_provider_service
from app.db.services.healthcare_provider_service import HealthcareProviderService
from app.schemas.healthcare_provider.schema import HealthcareProviderDto

router = APIRouter(prefix="/healthcare-providers", tags=["healthcare providers"])


@router.get(
    "/{id}",
    summary="Get one healthcare provider by ID",
)
def get(
    id_: UUID = Path(alias="id"),
    service: HealthcareProviderService = Depends(get_healthcare_provider_service),
) -> HealthcareProviderDto:
    return service.get(id_)
