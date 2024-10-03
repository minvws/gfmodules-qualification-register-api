from datetime import datetime
from uuid import UUID

import pytest
from sqlalchemy.orm import Session

from app.db.entities import (
    Application,
    ApplicationVersion,
    ApplicationVersionQualification,
    Protocol,
    ProtocolVersion,
    Role,
    SystemType,
    Vendor,
)
from app.schemas.application_summary.schema import ApplicationSummaryDto
from app.schemas.roles.schema import RoleDto
from app.schemas.system_type.schema import SystemTypeDto
from app.schemas.vendor.schema import VendorDto
from app.schemas.vendor_qualifications.schema import QualifiedVendorDTO


@pytest.fixture
def vendor_dto(session: Session, vendor: Vendor) -> VendorDto:
    with session.begin():
        session.add(vendor)
    return VendorDto(
        id=vendor.id,
        kvk_number=vendor.kvk_number,
        trade_name=vendor.trade_name,
        statutory_name=vendor.statutory_name,
        applications=[],
    )


@pytest.fixture
def role_dto(session: Session, role: Role) -> RoleDto:
    with session.begin():
        session.add(role)
    return RoleDto(id=role.id, name=role.name, description=role.description)


@pytest.fixture
def system_type_dto(session: Session, system_type: SystemType) -> SystemTypeDto:
    with session.begin():
        session.add(system_type)
    return SystemTypeDto(
        id=system_type.id, name=system_type.name, description=system_type.description
    )


@pytest.fixture
def vendor_qualification_dto(
    session: Session,
    vendor: Vendor,
    application: Application,
    application_version: ApplicationVersion,
    system_type: SystemType,
    role: Role,
    protocol: Protocol,
    application_version_qualification: ApplicationVersionQualification,
    protocol_version: ProtocolVersion,
) -> QualifiedVendorDTO:
    with session.begin():
        session.add(application_version_qualification)

    return QualifiedVendorDTO(
        qualification_id=application_version_qualification.id,
        application_version_id=application_version.id,
        application_id=application.id,
        vendor_id=vendor.id,
        protocol_id=protocol.id,
        system_type_id=system_type.id,
        role_id=role.id,
        application_version=application_version.version,
        application=application.name,
        protocol=protocol.name,
        protocol_version=protocol_version.version,
        system_type=system_type.name,
        role=role.name,
        kvk_number=vendor.kvk_number,
        trade_name=vendor.trade_name,
        statutory_name=vendor.statutory_name,
        qualification_date=application_version_qualification.qualification_date,
    )


@pytest.fixture
def vendors(session: Session, vendor: Vendor) -> tuple[Vendor, Vendor]:
    vendor_b = Vendor(
        id=UUID("7d09ac51-74b2-4c54-86e8-ad6122c2fd23"),
        kvk_number="000000002",
        trade_name="Vendor B - Trade Name",
        statutory_name="Vendor B - Statutory Name",
    )
    with session.begin():
        session.bulk_save_objects([vendor, vendor_b])
    return vendor, vendor_b


@pytest.fixture
def applications(
    session: Session, vendors: tuple[Vendor, Vendor]
) -> tuple[Application, Application, Application, Application]:
    _datetime = datetime.now()
    vendor_a, vendor_b = vendors
    applications = (
        Application(
            id=UUID("d63743c0-e327-4852-b4d3-0446bf5a4de3"),
            name="Application A - Vendor A",
            created_at=_datetime,
            modified_at=_datetime,
            vendor_id=vendor_a.id,
        ),
        Application(
            id=UUID("bab54458-6fa6-4832-acf9-a33aad89ab07"),
            name="Application B - Vendor A",
            created_at=_datetime,
            modified_at=_datetime,
            vendor_id=vendor_a.id,
        ),
        Application(
            id=UUID("a27d50e0-829e-474e-ba71-90e219fcc078"),
            name="Application A - Vendor B",
            created_at=_datetime,
            modified_at=_datetime,
            vendor_id=vendor_b.id,
        ),
        Application(
            id=UUID("be61c0ff-760c-4d59-b60d-8f907b6bca22"),
            name="Application B - Vendor B",
            created_at=_datetime,
            modified_at=_datetime,
            vendor_id=vendor_b.id,
        ),
    )
    vendor_a.applications = [applications[0], applications[1]]
    vendor_b.applications = [applications[2], applications[3]]
    with session.begin():
        session.bulk_save_objects(applications)

    return applications


@pytest.fixture
def vendor_dtos(vendors: tuple[Vendor, Vendor]) -> tuple[VendorDto, VendorDto]:
    vendor_a, vendor_b = vendors
    return (
        VendorDto(
            id=vendor_a.id,
            kvk_number=vendor_a.kvk_number,
            trade_name=vendor_a.trade_name,
            statutory_name=vendor_a.statutory_name,
            applications=[],
        ),
        VendorDto(
            id=vendor_b.id,
            kvk_number=vendor_b.kvk_number,
            trade_name=vendor_b.trade_name,
            statutory_name=vendor_b.statutory_name,
            applications=[],
        ),
    )


@pytest.fixture
def vendor_with_applications_dtos(
    applications: tuple[Application, Application, Application, Application],
    vendor_dtos: tuple[VendorDto, VendorDto],
) -> tuple[VendorDto, VendorDto]:
    app_a_vendor_a, app_b_vendor_a, app_a_vendor_b, app_b_vendor_b = applications

    vendor_dtos[0].applications = [
        ApplicationSummaryDto(
            id=app_a_vendor_a.id,
            name=app_a_vendor_a.name,
            created_at=app_a_vendor_a.created_at,
            modified_at=app_a_vendor_a.modified_at,
        ),
        ApplicationSummaryDto(
            id=app_b_vendor_a.id,
            name=app_b_vendor_a.name,
            created_at=app_b_vendor_a.created_at,
            modified_at=app_b_vendor_a.modified_at,
        ),
    ]
    vendor_dtos[1].applications = [
        ApplicationSummaryDto(
            id=app_a_vendor_b.id,
            name=app_a_vendor_b.name,
            created_at=app_a_vendor_b.created_at,
            modified_at=app_a_vendor_b.modified_at,
        ),
        ApplicationSummaryDto(
            id=app_b_vendor_b.id,
            name=app_b_vendor_b.name,
            created_at=app_b_vendor_b.created_at,
            modified_at=app_b_vendor_b.modified_at,
        ),
    ]
    return vendor_dtos
