from datetime import date
from typing import cast
from uuid import UUID

import pytest

from app.db.entities import (
    Application,
    ApplicationRole,
    ApplicationType,
    ApplicationVersion,
    Role,
    SystemType,
    Vendor,
)
from app.db.entities.application_version_qualification import (
    ApplicationVersionQualification,
)
from app.db.entities.protocol import Protocol
from app.db.services import (
    ApplicationService,
    HealthcareProviderService,
    RoleService,
    SystemTypeService,
    VendorQualificationService,
    VendorService,
)
from tests.utests.db.utils import Services


@pytest.fixture
def vendor_service() -> VendorService:
    return cast(VendorService, Services.VENDOR.get_instance())


@pytest.fixture
def role_service() -> RoleService:
    return cast(RoleService, Services.ROLE.get_instance())


@pytest.fixture
def system_type_service() -> SystemTypeService:
    return cast(SystemTypeService, Services.SYSTEM_TYPE.get_instance())


@pytest.fixture
def application_service() -> ApplicationService:
    return cast(ApplicationService, Services.APPLICATION.get_instance())


@pytest.fixture
def healthcare_provider_service() -> HealthcareProviderService:
    return cast(HealthcareProviderService, Services.HEALTHCARE_PROVIDER.get_instance())


@pytest.fixture
def vendor_qualification_service() -> VendorQualificationService:
    return cast(
        VendorQualificationService, Services.VENDOR_QUALIFICATION.get_instance()
    )


@pytest.fixture
def vendor() -> Vendor:
    return Vendor(
        id=UUID("eb213a0f-245e-4ffb-adaa-cecd3fcb30aa"),
        kvk_number="000000001",
        trade_name="Vendor A - Trade Name",
        statutory_name="Vendor A - Statutory Name",
    )


@pytest.fixture
def application_version() -> ApplicationVersion:
    return ApplicationVersion(
        id=UUID("abe43e15-c7bd-456c-aa82-7500275d72d5"), version="example"
    )


@pytest.fixture
def system_type() -> SystemType:
    return SystemType(id=UUID("27f358c3-9a9b-499b-b829-a0b08405c5b5"), name="example")


@pytest.fixture
def application(
    vendor: Vendor,
    application_version: ApplicationVersion,
    system_type: SystemType,
    role: Role,
) -> Application:
    entity = Application(
        id=UUID("33e821f7-bf51-46cc-a52c-fd17d7e6acda"),
        name="example",
        vendor=vendor,
        versions=[application_version],
        system_types=[],
        roles=[],
    )
    entity.system_types.append(
        ApplicationType(
            id=UUID("dad7cf44-7579-4f60-8114-22fec546f53f"),
            application=entity,
            system_type=system_type,
        )
    )
    entity.roles.append(
        ApplicationRole(
            id=UUID("45664631-4b4c-4191-b289-c97a0a7bb135"),
            application=entity,
            role=role,
        )
    )
    return entity


@pytest.fixture
def application_version_qualification(
    application: Application, protocol: Protocol
) -> ApplicationVersionQualification:
    return ApplicationVersionQualification(
        id=UUID("25e1a678-0082-456e-9538-6fe25316257c"),
        application_version=application.versions[0],
        protocol_version=protocol.versions[0],
        qualification_date=date.today(),
    )
