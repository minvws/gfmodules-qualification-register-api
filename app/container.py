import inject

from gfmodules_python_shared.session.session_factory import DbSessionFactory
from gfmodules_python_shared.repository.repository_factory import RepositoryFactory

from app.db.db import Database
from app.config import get_config
from app.db.services.application_database_service import (
    ApplicationDatabaseService,
)
from app.db.services.healthcare_provider_database_service import (
    HealthcareProviderDatabaseService,
)
from app.db.services.role_database_service import (
    RoleDatabaseService,
)
from app.db.services.system_type_database_service import (
    SystemTypeDatabaseService,
)
from app.db.services.vendor_database_service import (
    VendorDatabaseService,
)


def container_config(binder: inject.Binder) -> None:
    config = get_config()

    db = Database(dsn=config.database.dsn)
    binder.bind(Database, db)

    db_session_factory = DbSessionFactory(db.engine)
    binder.bind(DbSessionFactory, db_session_factory)

    healthcare_provider_database_service = HealthcareProviderDatabaseService()
    binder.bind(HealthcareProviderDatabaseService, healthcare_provider_database_service)

    application_database_service = ApplicationDatabaseService()
    binder.bind(ApplicationDatabaseService, application_database_service)

    repository_factory = RepositoryFactory(db.engine)
    binder.bind(RepositoryFactory, repository_factory)

    role_database_service = RoleDatabaseService()
    binder.bind(RoleDatabaseService, role_database_service)

    system_type_database_service = SystemTypeDatabaseService()
    binder.bind(SystemTypeDatabaseService, system_type_database_service)

    vendor_database_service = VendorDatabaseService()
    binder.bind(VendorDatabaseService, vendor_database_service)


def get_database() -> Database:
    return inject.instance(Database)


def get_healthcare_provider_database_service() -> (
    HealthcareProviderDatabaseService
):
    return inject.instance(HealthcareProviderDatabaseService)


def get_application_database_service() -> ApplicationDatabaseService:
    return inject.instance(ApplicationDatabaseService)


def get_role_database_service() -> RoleDatabaseService:
    return inject.instance(RoleDatabaseService)


def get_vendor_database_service() -> VendorDatabaseService:
    return inject.instance(VendorDatabaseService)


def get_system_type_database_service() -> SystemTypeDatabaseService:
    return inject.instance(SystemTypeDatabaseService)


if not inject.is_configured():
    inject.configure(container_config)
