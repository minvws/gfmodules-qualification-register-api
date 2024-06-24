
import inject

from app.db.db_session_factory import DbSessionFactory
from app.db.repository_factory import RepositoryFactory
from app.db.services.application_database_service import (
    ApplicationDatabaseService,
    ApplicationDatabaseServiceInterface,
)
from app.db.services.healthcare_provider_database_service import (
    HealthcareProviderDatabaseService,
    HealthcareProviderDatabaseServiceInterface,
)
from app.db.services.role_database_service import (
    RoleDatabaseService,
    RoleDatabaseServiceInterface,
)
from app.db.services.system_type_database_service import (
    SystemTypeDatabaseService,
    SystemTypeDatabaseServiceInterface,
)
from app.db.services.vendor_database_service import (
    VendorDatabaseService,
    VendorDatabaseServiceInterface,
)
from db.db import Database
from config import get_config


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
    HealthcareProviderDatabaseServiceInterface
):
    return inject.instance(HealthcareProviderDatabaseService)


def get_application_database_service() -> ApplicationDatabaseServiceInterface:
    return inject.instance(ApplicationDatabaseService)


def get_role_database_service() -> RoleDatabaseServiceInterface:
    return inject.instance(RoleDatabaseService)


def get_vendor_database_service() -> VendorDatabaseServiceInterface:
    return inject.instance(VendorDatabaseService)


def get_system_type_database_service() -> SystemTypeDatabaseServiceInterface:
    return inject.instance(SystemTypeDatabaseService)


if not inject.is_configured():
    inject.configure(container_config)
