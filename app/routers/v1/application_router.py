import logging
import uuid
from typing import Sequence

from fastapi import APIRouter, Depends, Path

from app.container import get_application_database_service
from app.db.services.application_database_service import (
    ApplicationDatabaseServiceInterface,
)
from app.dto.ApplicationWithVendorDto import ApplicationWithVendorDto

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/applications", tags=["applications"])


@router.get("", summary="Get all applications")
def get_all(
    application_database_service: ApplicationDatabaseServiceInterface = Depends(
        get_application_database_service
    ),
) -> Sequence[ApplicationWithVendorDto]:
    return application_database_service.get_all()


@router.get("/{id}", summary="Get application by id")
def get(
    id_: uuid.UUID = Path(alias="id"),
    application_database_service: ApplicationDatabaseServiceInterface = Depends(
        get_application_database_service
    ),
) -> ApplicationWithVendorDto:
    return application_database_service.get(id_)
