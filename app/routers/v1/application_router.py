import logging
import uuid
from typing import List

from fastapi import APIRouter, Depends, Path

from app.container import get_application_service
from app.db.services.application_service import ApplicationService
from app.openapi.responses import api_version_header_responses
from app.schemas.application.schema import ApplicationWithVendorDto

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/applications", tags=["applications"])


@router.get("", summary="Get all applications", responses={**api_version_header_responses([200])})
def get_all(
    application_service: ApplicationService = Depends(
        get_application_service
    ),
) -> List[ApplicationWithVendorDto]:
    return application_service.get_all()


@router.get("/{id}", summary="Get application by id", responses={**api_version_header_responses([200, 404, 422])})
def get(
    id_: uuid.UUID = Path(alias="id"),
    application_service: ApplicationService = Depends(
        get_application_service
    ),
) -> ApplicationWithVendorDto:
    return application_service.get(id_)
