import inject
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.config import get_config
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

    engine = create_engine(
        config.database.dsn, echo=False, pool_recycle=25, pool_size=10
    )
    binder.bind(Engine, engine)
    binder.bind(sessionmaker[Session], sessionmaker(engine))

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


def get_engine() -> Engine:
    return inject.instance(Engine)


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
