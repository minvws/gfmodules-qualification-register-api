from typing import Sequence

from app.db.entities.application import Application
from app.db.entities.application_version import ApplicationVersion
from app.schemas.application.schema import (
    ApplicationVersionDto, ApplicationWithVendorDto,
)
from app.schemas.roles.mapper import map_role_entity_to_dto
from app.schemas.system_type.mapper import map_system_type_entity_to_dto
from app.schemas.vendor.mapper import map_vendor_entity_to_summary_dto


def map_application_entities_to_dtos(
        entities: Sequence[Application],
) -> Sequence[ApplicationWithVendorDto]:
    return [map_application_entity_to_dto(entity) for entity in entities]


def map_application_entity_to_dto(entity: Application) -> ApplicationWithVendorDto:
    return ApplicationWithVendorDto(
        id=entity.id,
        name=entity.name,
        created_at=entity.created_at,
        modified_at=entity.modified_at,
        vendor=map_vendor_entity_to_summary_dto(entity.vendor),
        versions=[
            map_application_version_to_dto(version)
            for version in entity.versions
        ],
        roles=[map_role_entity_to_dto(role.role) for role in entity.roles],
        system_types=[
            map_system_type_entity_to_dto(system_type.system_type)
            for system_type in entity.system_types
        ],
    )


def map_application_version_to_dto(entity: ApplicationVersion) -> ApplicationVersionDto:
    return ApplicationVersionDto(
        id=entity.id,
        version=entity.version,
    )
