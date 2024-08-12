from datetime import datetime

from uuid import uuid4

from app.db.entities.application import Application
from app.db.entities.application_role import ApplicationRole
from app.db.entities.application_type import ApplicationType
from app.db.entities.application_version import ApplicationVersion
from app.db.entities.role import Role
from app.db.entities.system_type import SystemType
from app.db.entities.vendor import Vendor
from app.schemas.application.mapper import map_application_version_entity_to_dto, map_application_entity_to_dto
from app.schemas.application.schema import ApplicationVersionDto, ApplicationWithVendorDto
from app.schemas.roles.mapper import map_role_entity_to_dto
from app.schemas.system_type.mapper import map_system_type_entity_to_dto
from app.schemas.vendor.mapper import map_vendor_entity_to_summary_dto


def test_map_application_version_entity_to_dto() -> None:
    expected_uuid = uuid4()
    expected_version = "1"

    expected_application_version_dto = ApplicationVersionDto(
        id=expected_uuid,
        version=expected_version,
    )

    application_version = ApplicationVersion(
        id=expected_uuid,
        version=expected_version,
    )

    result = map_application_version_entity_to_dto(application_version)
    assert result == expected_application_version_dto


def test_map_application_entity_to_dto() -> None:
    expected_uuid = uuid4()
    expected_name = "Example application"
    expected_created_at = datetime.now()
    expected_modified_at = datetime.now()

    vendor = Vendor(
        id=uuid4(),
        trade_name="Example vendor",
        statutory_name="Example vendor statutory name",
        kvk_number="12345678",
        applications=[],
    )

    version = ApplicationVersion(
        id=uuid4(),
        version="1",
    )

    role = Role(
        id=uuid4(),
        name="Example role",
        description="Example role description",
    )

    application_role = ApplicationRole(
        id=uuid4(),
        role=role,
    )

    system_type = SystemType(
        id=uuid4(),
        name="Example system type",
        description="Example system type description",
        applications=[],
    )

    application_system_type = ApplicationType(
        id=uuid4(),
        system_type=system_type,
    )

    expected_application_dto = ApplicationWithVendorDto(
        id=expected_uuid,
        name=expected_name,
        created_at=expected_created_at,
        modified_at=expected_modified_at,
        vendor=map_vendor_entity_to_summary_dto(vendor),
        versions=[map_application_version_entity_to_dto(version)],
        roles=[map_role_entity_to_dto(role)],
        system_types=[map_system_type_entity_to_dto(system_type)],
    )

    application = Application(
        id=expected_uuid,
        name=expected_name,
        created_at=expected_created_at,
        modified_at=expected_modified_at,
        vendor=vendor,
        versions=[version],
        system_types=[application_system_type],
        roles=[application_role],
    )

    result = map_application_entity_to_dto(application)
    assert result == expected_application_dto

