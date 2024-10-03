import datetime
from uuid import UUID

import pytest
from gfmodules_python_shared.schema.pagination.page_schema import Page
from sqlalchemy.orm import Session

from app.db.entities import (
    Application,
    ApplicationVersion,
    ApplicationVersionQualification,
    HealthcareProvider,
    HealthcareProviderApplicationVersion,
    HealthcareProviderQualification,
    Protocol,
    ProtocolVersion,
)
from app.db.services import HealthcareProviderService
from app.exceptions.http_base_exceptions import NotFoundException
from app.schemas.healthcare_provider.schema import HealthcareProviderDto
from app.schemas.healthcare_provider_qualification.schema import (
    QualifiedHealthcareProviderDTO,
)


def test_get_qualified_healthcare_providers_should_succeed(
    session: Session,
    healthcare_provider: HealthcareProvider,
    protocol: Protocol,
    protocol_version: ProtocolVersion,
    application: Application,
    application_version: ApplicationVersion,
    healthcare_provider_service: HealthcareProviderService,
):
    healthcare_provider_qualification = HealthcareProviderQualification(
        healthcare_provider=healthcare_provider,
        protocol_version=protocol_version,
        qualification_date=datetime.date.today(),
    )
    provider_application_version = HealthcareProviderApplicationVersion(
        healthcare_provider=healthcare_provider,
        application_version=application_version,
    )
    application_qualification = ApplicationVersionQualification(
        application_version=application_version,
        protocol_version=protocol_version,
        qualification_date=datetime.date.today(),
    )
    protocol_version.qualified_application_versions.append(application_qualification)
    healthcare_provider.application_versions.append(provider_application_version)

    with session.begin():
        session.add(application)
        session.add(healthcare_provider)

    data = [
        QualifiedHealthcareProviderDTO(
            qualification_id=healthcare_provider_qualification.id,
            healthcare_provider_id=healthcare_provider.id,
            protocol_id=protocol.id,
            protocol_version_id=protocol_version.id,
            healthcare_provider=healthcare_provider.trade_name,
            protocol=protocol.name,
            protocol_type=protocol.protocol_type,
            protocol_version=protocol_version.version,
            qualification_date=healthcare_provider_qualification.qualification_date,
        )
    ]
    assert healthcare_provider_service.get_qualified_healthcare_providers(
        limit=10, offset=0
    ) == Page(items=data, limit=10, offset=0, total=1)


def get_should_succeed(
    session: Session,
    healthcare_provider: HealthcareProvider,
    healthcare_provider_service: HealthcareProviderService,
):
    with session.begin():
        session.add(healthcare_provider)

    assert healthcare_provider_service.get(
        provider_id=healthcare_provider.id
    ) == HealthcareProviderDto(
        id=healthcare_provider.id,
        ura_code=healthcare_provider.ura_code,
        agb_code=healthcare_provider.agb_code,
        trade_name=healthcare_provider.trade_name,
        statutory_name=healthcare_provider.statutory_name,
    )


def get_should_fail_when_provided_incorrect_id(
    session: Session,
    healthcare_provider: HealthcareProvider,
    healthcare_provider_service: HealthcareProviderService,
):
    with session.begin():
        session.add(healthcare_provider)

    with pytest.raises(NotFoundException):
        healthcare_provider_service.get(
            provider_id=UUID("b272e0ad-c9e9-4899-9243-52a3fe543454")
        )


def get_paginated_should_succeed(
    session: Session,
    healthcare_provider: HealthcareProvider,
    healthcare_provider_service: HealthcareProviderService,
):
    with session.begin():
        session.add(healthcare_provider)
    data = HealthcareProviderDto(
        id=healthcare_provider.id,
        ura_code=healthcare_provider.ura_code,
        agb_code=healthcare_provider.agb_code,
        trade_name=healthcare_provider.trade_name,
        statutory_name=healthcare_provider.statutory_name,
    )
    assert healthcare_provider_service.get_paginated(limit=10, offset=0) == Page(
        items=[data], limit=10, offset=0, total=1
    )
