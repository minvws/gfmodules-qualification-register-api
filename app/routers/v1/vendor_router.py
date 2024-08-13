import uuid
from typing import List

from fastapi import APIRouter, Depends, Path

from app.container import get_vendor_service
from app.db.services.vendor_service import VendorService
from app.openapi.responses import api_version_header_responses
from app.schemas.vendor.schema import VendorDto

router = APIRouter(prefix="/vendors", tags=["vendors"])


@router.get("", summary="Get all vendors", responses={**api_version_header_responses([200])})
def get_all(
        vendor_service: VendorService = Depends(
            get_vendor_service
        ),
) -> List[VendorDto]:
    return vendor_service.get_all()


@router.get("/{id}", summary="Get vendor by id", responses={**api_version_header_responses([200, 404, 422])})
def get(
        id_: uuid.UUID = Path(alias="id"),
        vendor_service: VendorService = Depends(
            get_vendor_service
        ),
) -> VendorDto:
    return vendor_service.get(id_)
