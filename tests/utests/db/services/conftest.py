from typing import Generator, Any

import inject
import pytest
from gfmodules_python_shared.repository.repository_factory import RepositoryFactory
from gfmodules_python_shared.session.db_session import DbSession
from gfmodules_python_shared.session.session_factory import DbSessionFactory

from app.db.db import Database
from app.db.repository.application_repository import ApplicationRepository
from app.db.repository.application_version_qualification_repository import (
    ApplicationVersionQualificationRepository,
)
from app.db.repository.healthcare_provider_repository import (
    HealthcareProviderRepository,
)
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
def healthcare_provider_service(session: DbSession) -> HealthcareProviderService:
    return HealthcareProviderService()


@pytest.fixture
def healthcare_provider_repository(session: DbSession) -> HealthcareProviderRepository:
    return HealthcareProviderRepository(db_session=session)


@pytest.fixture
def role_service(session: DbSession) -> RoleService:
    return RoleService()


@pytest.fixture
def role_repository(session: DbSession) -> RoleRepository:
    return RoleRepository(db_session=session)


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
