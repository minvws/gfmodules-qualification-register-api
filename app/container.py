import inject

from gfmodules_python_shared.session.session_factory import DbSessionFactory
from gfmodules_python_shared.repository.repository_factory import RepositoryFactory

from app.db.db import Database
from app.config import get_config
from app.db.services.application_service import (
    ApplicationService,
)
from app.db.services.healthcare_provider_service import (
    HealthcareProviderService,
)
from app.db.services.role_service import (
    RoleService,
)
from app.db.services.system_type_service import (
    SystemTypeService,
)
from app.db.services.vendor_service import (
    VendorService,
)


def container_config(binder: inject.Binder) -> None:
    config = get_config()

    db = Database(dsn=config.database.dsn)
    binder.bind(Database, db)

    session_factory = DbSessionFactory(db.engine)
    binder.bind(DbSessionFactory, session_factory)

    repository_factory = RepositoryFactory()
    binder.bind(RepositoryFactory, repository_factory)

    healthcare_provider_service = HealthcareProviderService()
    binder.bind(HealthcareProviderService, healthcare_provider_service)

    application_service = ApplicationService()
    binder.bind(ApplicationService, application_service)

    role_service = RoleService()
    binder.bind(RoleService, role_service)

    system_type_service = SystemTypeService()
    binder.bind(SystemTypeService, system_type_service)

    vendor_service = VendorService()
    binder.bind(VendorService, vendor_service)


def get_database() -> Database:
    return inject.instance(Database)


def get_healthcare_provider_service() -> (
    HealthcareProviderService
):
    return inject.instance(HealthcareProviderService)


def get_application_service() -> ApplicationService:
    return inject.instance(ApplicationService)


def get_role_service() -> RoleService:
    return inject.instance(RoleService)


def get_vendor_service() -> VendorService:
    return inject.instance(VendorService)


def get_system_type_service() -> SystemTypeService:
    return inject.instance(SystemTypeService)


if not inject.is_configured():
    inject.configure(container_config)
