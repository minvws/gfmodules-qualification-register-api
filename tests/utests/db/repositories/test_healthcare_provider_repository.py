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
def protocol_version() -> ProtocolVersion:
    return ProtocolVersion(id=uuid4(), version="example")


@pytest.fixture
def protocol(protocol_version: ProtocolVersion) -> Protocol:
    return Protocol(
        id=uuid4(),
        protocol_type="InformationStandard",
        name="example",
        versions=[protocol_version],
    )


@pytest.fixture
def healthcare_provider() -> HealthcareProvider:
    return HealthcareProvider(
        id=uuid4(),
        ura_code="example",
        agb_code="example",
        trade_name="example",
        statutory_name="example",
    )


@pytest.fixture
def qualification(
    protocol_version: ProtocolVersion, healthcare_provider: HealthcareProvider
) -> HealthcareProviderQualification:
    return HealthcareProviderQualification(
        id=uuid4(),
        protocol_version=protocol_version,
        healthcare_provider=healthcare_provider,
        qualification_date=date.today(),
    )


def test_get_healthcare_provider_qualifications_should_succeed(
    healthcare_provider_repository: HealthcareProviderRepository,
    protocol_repository: ProtocolRepository,
    healthcare_provider: HealthcareProvider,
    protocol: Protocol,
    protocol_version: ProtocolVersion,
    qualification: HealthcareProviderQualification,
) -> None:
    healthcare_provider.qualified_protocols.append(qualification)
    expected_qualified_providers = [
        {
            "qualification_id": qualification.id,
            "qualification_date": qualification.qualification_date,
            "protocol_id": protocol.id,
            "protocol_version_id": protocol_version.id,
            "healthcare_provider_id": healthcare_provider.id,
            "healthcare_provider": healthcare_provider.statutory_name,
            "protocol": protocol.name,
            "protocol_version": protocol_version.version,
            "protocol_type": protocol.protocol_type,
        }
    ]

    protocol_repository.create(protocol)
    healthcare_provider_repository.create(healthcare_provider)

    actual_qualified_providers = [
        row._mapping
        for row in (healthcare_provider_repository.get_qualified_providers())
    ]

    assert expected_qualified_providers == actual_qualified_providers


def test_get_healthcare_provider_qualification_should_return_empty_list_if_no_provider_is_qualified(
    healthcare_provider_repository: HealthcareProviderRepository,
    protocol_repository: ProtocolRepository,
    healthcare_provider: HealthcareProvider,
    protocol: Protocol,
) -> None:
    protocol_repository.create(protocol)
    healthcare_provider_repository.create(healthcare_provider)

    results = [
        row._mapping for row in healthcare_provider_repository.get_qualified_providers()
    ]

    expected_length = 0
    actual_length = len(results)

    assert isinstance(results, list)
    assert expected_length == actual_length


def test_get_healthcare_provider_qualification_should_return_results_exact_as_limit_provided(
    healthcare_provider_repository: HealthcareProviderRepository,
    protocol_repository: ProtocolRepository,
    healthcare_provider: HealthcareProvider,
    protocol: Protocol,
    protocol_version: ProtocolVersion,
    qualification: HealthcareProviderQualification,
) -> None:
    protocol_version_2 = ProtocolVersion(
        id=uuid4(),
        version="example 2",
    )
    qualification_2 = HealthcareProviderQualification(
        id=uuid4(),
        protocol_version=protocol_version_2,
        healthcare_provider=healthcare_provider,
        qualification_date=date.today(),
    )
    protocol.versions.append(protocol_version_2)
    healthcare_provider.qualified_protocols.append(qualification)
    healthcare_provider.qualified_protocols.append(qualification_2)
    protocol_repository.create(protocol)
    healthcare_provider_repository.create(healthcare_provider)

    expected_qualified_providers = [
        {
            "qualification_id": qualification.id,
            "qualification_date": qualification.qualification_date,
            "protocol_id": protocol.id,
            "protocol_version_id": protocol_version.id,
            "healthcare_provider_id": healthcare_provider.id,
            "healthcare_provider": healthcare_provider.statutory_name,
            "protocol": protocol.name,
            "protocol_version": protocol_version.version,
            "protocol_type": protocol.protocol_type,
        },
    ]
    actual_qualified_providers = [
        row._mapping
        for row in healthcare_provider_repository.get_qualified_providers(limit=1)
    ]

    assert expected_qualified_providers == actual_qualified_providers
    assert len(expected_qualified_providers) == len(actual_qualified_providers)


def test_get_healthcare_provider_qualifications_should_return_empty_list_if_offset_exceeds_the_results(
    healthcare_provider_repository: HealthcareProviderRepository,
    protocol_repository: ProtocolRepository,
    healthcare_provider: HealthcareProvider,
    protocol: Protocol,
) -> None:
    protocol_repository.create(protocol)
    healthcare_provider_repository.create(healthcare_provider)

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
    healthcare_provider_repository: HealthcareProviderRepository,
    protocol_repository: ProtocolRepository,
    protocol: Protocol,
):
    protocol_repository.create(protocol)

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
