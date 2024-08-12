from typing import Sequence, List

from app.db.entities.vendor import Vendor
from app.schemas.application_summary.mapper import map_application_entity_to_summary_dto
from app.schemas.vendor.schema import VendorDto, VendorSummaryDto


def map_vendor_entities_to_dtos(entities: Sequence[Vendor]) -> List[VendorDto]:
    return [map_vendor_entity_to_dto(entity) for entity in entities]


def map_vendor_entity_to_dto(entity: Vendor) -> VendorDto:
    return VendorDto(
        id=entity.id,
        trade_name=entity.trade_name,
        statutory_name=entity.statutory_name,
        kvk_number=entity.kvk_number,
        applications=[
            map_application_entity_to_summary_dto(application)
            for application in entity.applications
        ],
    )


def map_vendor_entity_to_summary_dto(entity: Vendor) -> VendorSummaryDto:
    return VendorSummaryDto(
        id=entity.id,
        trade_name=entity.trade_name,
        statutory_name=entity.statutory_name,
        kvk_number=entity.kvk_number,
    )
