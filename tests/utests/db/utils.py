from typing import Literal, Type
from gfmodules_python_shared.schema.sql_model import TSQLModel
from inject import Binder, instance
from sqlalchemy.orm import Session, sessionmaker

from app.db.db import Database
from app.db.services import (
    ApplicationService,
    HealthcareProviderService,
    RoleService,
    Service,
    SystemTypeService,
    VendorQualificationService,
    VendorService,
)


def container_config(binder: Binder) -> None:
    database = Database("sqlite:///:memory:", generate_tables=True)
    (
        binder.bind(Database, database)
        .bind(sessionmaker[Session], sessionmaker(database.engine))
        .bind(VendorService, VendorService())
        .bind(RoleService, RoleService())
        .bind(SystemTypeService, SystemTypeService())
        .bind(ApplicationService, ApplicationService())
        .bind(VendorQualificationService, VendorQualificationService())
        .bind(HealthcareProviderService, HealthcareProviderService())
    )


def _get_service_class(service: str) -> Type[Service]:
    match service:
        case "vendor":
            return VendorService
        case "vendor_qualification":
            return VendorQualificationService
        case "role":
            return RoleService
        case "system_type":
            return SystemTypeService
        case "application":
            return ApplicationService
        case "healthcare_provider":
            return HealthcareProviderService
        case _:
            raise ValueError(f"{service} is not supported")


def get_service(
    service: Literal[
        "vendor",
        "vendor_qualification",
        "role",
        "system_type",
        "application",
        "healthcare_provider",
    ],
) -> Service:
    return instance(_get_service_class(service))  # type: ignore


def are_the_same_entity(actual: TSQLModel, comparer: TSQLModel) -> bool:
    return all(
        getattr(actual, key) == getattr(comparer, key)
        for key in actual.__table__.columns.keys()  # noqa: SIM118
    )
