import datetime

import pytest
from gfmodules_python_shared.schema.pagination.page_schema import Page

from app.db.entities.application import Application
from app.db.entities.application_version import ApplicationVersion
from app.db.entities.application_version_qualification import (
    ApplicationVersionQualification,
)
from app.db.entities.healthcare_provider import HealthcareProvider
from app.db.entities.healthcare_provider_application_version import (
    HealthcareProviderApplicationVersion,
)
from app.db.entities.healthcare_provider_qualification import (
    HealthcareProviderQualification,
)
from app.db.entities.protocol import Protocol
from app.db.entities.protocol_version import ProtocolVersion
from app.db.repository.application_repository import ApplicationRepository
from app.db.repository.healthcare_provider_qualification_repository import (
    HealthcareProviderQualificationRepository,
)
from app.db.repository.healthcare_provider_repository import (
    HealthcareProviderRepository,
)
from app.db.repository.protocol_repository import ProtocolRepository
from app.db.services.healthcare_provider_service import HealthcareProviderService
from app.exceptions.http_base_exceptions import NotFoundException
from app.schemas.healthcare_provider.schema import HealthcareProviderDto
from app.schemas.healthcare_provider_qualification.schema import (
    QualifiedHealthcareProviderDTO,
)


class TestHealthcareProvidersService:

    def test_get_qualified_healthcare_providers_should_succeed(
        self,
        mock_healthcare_provider: HealthcareProvider,
        mock_protocol: Protocol,
        mock_protocol_version: ProtocolVersion,
        mock_application: Application,
        mock_application_version: ApplicationVersion,
        healthcare_provider_service: HealthcareProviderService,
        healthcare_provider_repository: HealthcareProviderRepository,
        healthcare_provider_qualification_repository: HealthcareProviderQualificationRepository,
        protocol_repository: ProtocolRepository,
        application_repository: ApplicationRepository,
    ):
        mock_healthcare_provider_qualification = HealthcareProviderQualification(
            healthcare_provider=mock_healthcare_provider,
            protocol_version=mock_protocol_version,
            qualification_date=datetime.date.today(),
        )
        provider_application_version = HealthcareProviderApplicationVersion(
            healthcare_provider=mock_healthcare_provider,
            application_version=mock_application_version,
        )
        mock_application_qualification = ApplicationVersionQualification(
            application_version=mock_application_version,
            protocol_version=mock_protocol_version,
            qualification_date=datetime.date.today(),
        )
        mock_protocol_version.qualified_application_versions.append(
            mock_application_qualification
        )
        mock_healthcare_provider.application_versions.append(
            provider_application_version
        )

        application_repository.create(mock_application)
        protocol_repository.create(mock_protocol)
        healthcare_provider_repository.create(mock_healthcare_provider)
        healthcare_provider_qualification_repository.create(
            mock_healthcare_provider_qualification
        )
        data = [
            QualifiedHealthcareProviderDTO(
                provider_id=mock_healthcare_provider.id,
                provider_name=mock_protocol.name,
                protocol=mock_protocol.name,
                protocol_version=mock_protocol_version.version,
                application_name=mock_application.name,
                application_version=mock_application_version.version,
                qualification_date=mock_healthcare_provider_qualification.qualification_date,
            )
        ]
        expected_qualified_providers = Page(
            items=data,
            limit=10,
            offset=0,
            total=1,
        )
        actual_qualified_providers = (
            healthcare_provider_service.get_qualified_healthcare_providers(
                limit=10, offset=0
            )
        )

        assert expected_qualified_providers == actual_qualified_providers

    def get_should_succeed(
        self,
        mock_healthcare_provider: HealthcareProvider,
        healthcare_provider_service: HealthcareProviderService,
        healthcare_provider_repository: HealthcareProviderRepository,
    ):
        healthcare_provider_repository.create(mock_healthcare_provider)

        expected_healthcare_provider = HealthcareProviderDto(
            id=mock_healthcare_provider.id,
            ura_code=mock_healthcare_provider.ura_code,
            agb_code=mock_healthcare_provider.agb_code,
        )
        actual_healthcare_provider = healthcare_provider_service.get(
            provider_id=mock_healthcare_provider.id
        )

        assert expected_healthcare_provider == actual_healthcare_provider

    def get_should_fail_when_provided_incorrect_id(
        self,
        mock_healthcare_provider: HealthcareProvider,
        healthcare_provider_service: HealthcareProviderService,
        healthcare_provider_repository: HealthcareProviderRepository,
    ):
        healthcare_provider_repository.create(mock_healthcare_provider)
        with pytest.raises(NotFoundException):
            healthcare_provider_service.get(provider_id="some wrong id")
