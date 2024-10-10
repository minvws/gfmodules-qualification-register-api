import re
from enum import StrEnum, auto
from typing import Type

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


class Services(StrEnum):
    APPLICATION = auto()
    HEALTHCARE_PROVIDER = auto()
    ROLE = auto()
    SYSTEM_TYPE = auto()
    VENDOR = auto()
    VENDOR_QUALIFICATION = auto()

    @property
    def _to_pascal_case(self) -> str:
        return re.sub(
            r"(^|_)([a-z])", lambda match: match.group(2).upper(), self.lower()
        )

    @property
    def _service_type(self) -> Type[Service]:
        return eval(f"{self._to_pascal_case}Service")  # type: ignore

    def get_instance(self) -> Service:
        return instance(self._service_type)  # type: ignore


def are_the_same_entity(actual: TSQLModel, comparer: TSQLModel) -> bool:
    return all(
        getattr(actual, key) == getattr(comparer, key)
        for key in actual.__table__.columns.keys()  # noqa: SIM118
    )
