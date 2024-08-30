from datetime import date

import pytest
from uuid import uuid4

from app.db.entities.healthcare_provider import HealthcareProvider
from app.db.entities.healthcare_provider_qualification import (
    HealthcareProviderQualification,
)
from app.db.entities.protocol import Protocol
from app.db.entities.protocol_version import ProtocolVersion
from app.db.repository.healthcare_provider_repository import (
    HealthcareProviderRepository,
)
from app.db.repository.protocol_repository import ProtocolRepository


@pytest.fixture
def mock_protocol_version() -> ProtocolVersion:
    return ProtocolVersion(id=uuid4(), version="example")


@pytest.fixture
def mock_protocol(mock_protocol_version: ProtocolVersion) -> Protocol:
    return Protocol(
        id=uuid4(),
        protocol_type="InformationStandard",
        name="example",
        versions=[mock_protocol_version],
    )


@pytest.fixture
def mock_healthcare_provider() -> HealthcareProvider:
    return HealthcareProvider(
        id=uuid4(),
        ura_code="example",
        agb_code="example",
        trade_name="example",
        statutory_name="example",
    )


@pytest.fixture
def mock_qualification(
    mock_protocol_version: ProtocolVersion, mock_healthcare_provider: HealthcareProvider
) -> HealthcareProviderQualification:
    return HealthcareProviderQualification(
        id=uuid4(),
        protocol_version=mock_protocol_version,
        healthcare_provider=mock_healthcare_provider,
        qualification_date=date.today(),
    )


class TestHealthcareProviderRepository:
    def test_get_healthcare_provider_qualifications_should_succeed(
        self,
        healthcare_provider_repository: HealthcareProviderRepository,
        protocol_repository: ProtocolRepository,
        mock_healthcare_provider: HealthcareProvider,
        mock_protocol: Protocol,
        mock_protocol_version: ProtocolVersion,
        mock_qualification: HealthcareProviderQualification,
    ) -> None:
        mock_healthcare_provider.qualified_protocols.append(mock_qualification)
        expected_qualified_providers = [
            {
                "qualification_id": mock_qualification.id,
                "qualification_date": mock_qualification.qualification_date,
                "protocol_id": mock_protocol.id,
                "protocol_version_id": mock_protocol_version.id,
                "healthcare_provider_id": mock_healthcare_provider.id,
                "healthcare_provider": mock_healthcare_provider.statutory_name,
                "protocol": mock_protocol.name,
                "protocol_version": mock_protocol_version.version,
                "protocol_type": mock_protocol.protocol_type,
            }
        ]

        protocol_repository.create(mock_protocol)
        healthcare_provider_repository.create(mock_healthcare_provider)

        actual_qualified_providers = [
            row._mapping
            for row in (healthcare_provider_repository.get_qualified_providers())
        ]

        assert expected_qualified_providers == actual_qualified_providers

    def test_get_healthcare_provider_qualification_should_return_empty_list_if_no_provider_is_qualified(
        self,
        healthcare_provider_repository: HealthcareProviderRepository,
        protocol_repository: ProtocolRepository,
        mock_healthcare_provider: HealthcareProvider,
        mock_protocol: Protocol,
    ) -> None:
        protocol_repository.create(mock_protocol)
        healthcare_provider_repository.create(mock_healthcare_provider)

        results = [
            row._mapping
            for row in healthcare_provider_repository.get_qualified_providers()
        ]

        expected_length = 0
        actual_length = len(results)

        assert isinstance(results, list)
        assert expected_length == actual_length

    def test_get_healthcare_provider_qualification_should_return_results_exact_as_limit_provided(
        self,
        healthcare_provider_repository: HealthcareProviderRepository,
        protocol_repository: ProtocolRepository,
        mock_healthcare_provider: HealthcareProvider,
        mock_protocol: Protocol,
        mock_protocol_version: ProtocolVersion,
        mock_qualification: HealthcareProviderQualification,
    ) -> None:
        mock_protocol_version_2 = ProtocolVersion(
            id=uuid4(),
            version="example 2",
        )
        mock_qualification_2 = HealthcareProviderQualification(
            id=uuid4(),
            protocol_version=mock_protocol_version_2,
            healthcare_provider=mock_healthcare_provider,
            qualification_date=date.today(),
        )
        mock_protocol.versions.append(mock_protocol_version_2)
        mock_healthcare_provider.qualified_protocols.append(mock_qualification)
        mock_healthcare_provider.qualified_protocols.append(mock_qualification_2)
        protocol_repository.create(mock_protocol)
        healthcare_provider_repository.create(mock_healthcare_provider)

        expected_qualified_providers = [
            {
                "qualification_id": mock_qualification.id,
                "qualification_date": mock_qualification.qualification_date,
                "protocol_id": mock_protocol.id,
                "protocol_version_id": mock_protocol_version.id,
                "healthcare_provider_id": mock_healthcare_provider.id,
                "healthcare_provider": mock_healthcare_provider.statutory_name,
                "protocol": mock_protocol.name,
                "protocol_version": mock_protocol_version.version,
                "protocol_type": mock_protocol.protocol_type,
            },
        ]
        actual_qualified_providers = [
            row._mapping
            for row in healthcare_provider_repository.get_qualified_providers(limit=1)
        ]

        assert expected_qualified_providers == actual_qualified_providers
        assert len(expected_qualified_providers) == len(actual_qualified_providers)

    def test_get_healthcare_provider_qualifications_should_return_empty_list_if_offset_exceeds_the_results(
        self,
        healthcare_provider_repository: HealthcareProviderRepository,
        protocol_repository: ProtocolRepository,
        mock_healthcare_provider: HealthcareProvider,
        mock_protocol: Protocol,
    ) -> None:
        protocol_repository.create(mock_protocol)
        healthcare_provider_repository.create(mock_healthcare_provider)

        results = [
            row._mapping
            for row in healthcare_provider_repository.get_qualified_providers(
                offset=10, limit=10
            )
        ]

        expected_length = 0
        actual_length = len(results)

        assert isinstance(results, list)
        assert expected_length == actual_length

    def test_get_healthcare_provider_qualifications_should_return_empty_list_if_no_provider_exists(
        self,
        healthcare_provider_repository: HealthcareProviderRepository,
        protocol_repository: ProtocolRepository,
        mock_protocol: Protocol,
    ):
        protocol_repository.create(mock_protocol)

        results = [
            row._mapping
            for row in healthcare_provider_repository.get_qualified_providers(
                offset=10, limit=10
            )
        ]

        expected_length = 0
        actual_length = len(results)

        assert isinstance(results, list)
        assert expected_length == actual_length
