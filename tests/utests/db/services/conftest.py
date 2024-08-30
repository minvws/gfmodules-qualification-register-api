from typing import Generator, Any

import inject
import pytest
from gfmodules_python_shared.repository.repository_factory import RepositoryFactory
from gfmodules_python_shared.session.db_session import DbSession
from gfmodules_python_shared.session.session_factory import DbSessionFactory

from app.db.db import Database
from app.db.entities.application import Application
from app.db.entities.application_role import ApplicationRole
from app.db.entities.application_type import ApplicationType
from app.db.entities.application_version import ApplicationVersion
from app.db.entities.healthcare_provider import HealthcareProvider
from app.db.entities.protocol import Protocol
from app.db.entities.protocol_version import ProtocolVersion
from app.db.entities.role import Role
from app.db.entities.system_type import SystemType
from app.db.entities.vendor import Vendor
from app.db.repository.application_repository import ApplicationRepository
from app.db.repository.application_version_qualification_repository import (
    ApplicationVersionQualificationRepository,
)
from app.db.repository.healthcare_provider_qualification_repository import (
    HealthcareProviderQualificationRepository,
)
from app.db.repository.healthcare_provider_repository import (
    HealthcareProviderRepository,
)
from app.db.repository.protocol_repository import ProtocolRepository
from app.db.repository.role_repository import RoleRepository
from app.db.repository.system_type_repository import SystemTypeRepository
from app.db.repository.vendor_repository import VendorRepository
from app.db.services.application_service import ApplicationService
from app.db.services.healthcare_provider_service import HealthcareProviderService
from app.db.services.role_service import RoleService
from app.db.services.system_type_service import SystemTypeService
from app.db.services.vendor_qualification_service import VendorQualificationService
from app.db.services.vendor_service import VendorService


@pytest.fixture
def session() -> Generator[DbSession, Any, None]:
    db = Database("sqlite:///:memory:")
    db.generate_tables()
    session_factory = DbSessionFactory(db.engine)
    session = session_factory.create()

    repository_factory = RepositoryFactory()

    inject.configure(
        lambda binder: binder.bind(DbSessionFactory, session_factory).bind(  # type: ignore
            RepositoryFactory, repository_factory
        ),
        clear=True,
    )

    yield session


@pytest.fixture
def application_service(session: DbSession) -> ApplicationService:
    return ApplicationService()


@pytest.fixture
def application_repository(session: DbSession) -> ApplicationRepository:
    return ApplicationRepository(db_session=session)


@pytest.fixture
def healthcare_provider_repository(session: DbSession) -> HealthcareProviderRepository:
    return HealthcareProviderRepository(db_session=session)


@pytest.fixture
def healthcare_provider_service(session: DbSession) -> HealthcareProviderService:
    return HealthcareProviderService()


@pytest.fixture
def healthcare_provider_qualification_repository(
    session: DbSession,
) -> HealthcareProviderQualificationRepository:
    return HealthcareProviderQualificationRepository(db_session=session)


@pytest.fixture
def role_service(session: DbSession) -> RoleService:
    return RoleService()


@pytest.fixture
def role_repository(session: DbSession) -> RoleRepository:
    return RoleRepository(db_session=session)


@pytest.fixture
def protocol_repository(session: DbSession) -> ProtocolRepository:
    return ProtocolRepository(db_session=session)


@pytest.fixture
def application_version_qualification_repository(
    session: DbSession,
) -> ApplicationVersionQualificationRepository:
    return ApplicationVersionQualificationRepository(db_session=session)


@pytest.fixture
def system_type_service(session: DbSession) -> SystemTypeService:
    return SystemTypeService()


@pytest.fixture
def system_type_repository(session: DbSession) -> SystemTypeRepository:
    return SystemTypeRepository(db_session=session)


@pytest.fixture
def vendor_service(session: DbSession) -> VendorService:
    return VendorService()


@pytest.fixture
def vendor_repository(session: DbSession) -> VendorRepository:
    return VendorRepository(db_session=session)


@pytest.fixture
def vendor_qualification_service() -> VendorQualificationService:
    return VendorQualificationService()


@pytest.fixture
def mock_vendor() -> Vendor:
    return Vendor(
        kvk_number="example",
        trade_name="example",
        statutory_name="example",
    )


@pytest.fixture
def mock_application_version() -> ApplicationVersion:
    return ApplicationVersion(version="example")


@pytest.fixture
def mock_system_type() -> SystemType:
    return SystemType(name="example")


@pytest.fixture
def mock_role() -> Role:
    return Role(name="example")


@pytest.fixture
def mock_application(
    mock_vendor: Vendor,
    mock_application_version: ApplicationVersion,
    mock_system_type: SystemType,
    mock_role: Role,
) -> Application:
    mock_application = Application(
        name="example",
        vendor=mock_vendor,
        versions=[mock_application_version],
        system_types=[],
        roles=[],
    )
    mock_application_role = ApplicationRole(
        application=mock_application, role=mock_role
    )
    mock_application_type = ApplicationType(
        application=mock_application, system_type=mock_system_type
    )

    mock_application.system_types.append(mock_application_type)
    mock_application.roles.append(mock_application_role)
    return mock_application


@pytest.fixture
def mock_protocol_version() -> ProtocolVersion:
    return ProtocolVersion(version="example")


@pytest.fixture
def mock_protocol(mock_protocol_version: ProtocolVersion) -> Protocol:
    return Protocol(
        protocol_type="InformationStandard",
        name="example",
        versions=[mock_protocol_version],
    )


@pytest.fixture
def mock_healthcare_provider() -> HealthcareProvider:
    return HealthcareProvider(
        ura_code="example",
        agb_code="example",
        trade_name="example",
        statutory_name="example",
    )
