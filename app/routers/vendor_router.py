import uuid
from typing import Sequence

from fastapi import APIRouter, Depends, Path

from app.container import get_vendor_database_service
from app.db.services.vendor_database_service import (
    VendorDatabaseServiceInterface,
)
from app.dto.VendorDto import VendorDto

router = APIRouter(prefix="/vendors", tags=["vendors"])


@router.get("/", summary="Get all vendors")
def get_all(
    vendor_database_service: VendorDatabaseServiceInterface = Depends(
        get_vendor_database_service
    ),
) -> Sequence[VendorDto]:
    return vendor_database_service.get_all()


@router.get("/{id}", summary="Get vendor by id")
def get(
    id_: uuid.UUID = Path(alias="id"),
    vendor_database_service: VendorDatabaseServiceInterface = Depends(
        get_vendor_database_service
    ),
) -> VendorDto:
    return vendor_database_service.get(id_)
