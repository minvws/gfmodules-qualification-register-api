import inject
from sqlalchemy.orm import Session, sessionmaker

from app.config import get_config
from app.db.db import Database
from app.db.services import (
    ApplicationService,
    HealthcareProviderService,
    RoleService,
    SystemTypeService,
    VendorQualificationService,
    VendorService,
)


def container_config(binder: inject.Binder) -> None:
    config = get_config()

    db = Database(dsn=config.database.dsn)
    binder.bind(Database, db)

    binder.bind(sessionmaker[Session], sessionmaker(db.engine, expire_on_commit=False))

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

    vendor_qualification_service = VendorQualificationService()
    binder.bind(VendorQualificationService, vendor_qualification_service)


def get_database() -> Database:
    return inject.instance(Database)


def get_healthcare_provider_service() -> HealthcareProviderService:
    return inject.instance(HealthcareProviderService)


def get_application_service() -> ApplicationService:
    return inject.instance(ApplicationService)


def get_role_service() -> RoleService:
    return inject.instance(RoleService)


def get_vendor_service() -> VendorService:
    return inject.instance(VendorService)


def get_system_type_service() -> SystemTypeService:
    return inject.instance(SystemTypeService)


def get_vendor_qualification_service() -> VendorQualificationService:
    return inject.instance(VendorQualificationService)


if not inject.is_configured():
    inject.configure(container_config)
