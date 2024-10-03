from collections.abc import Callable, Iterable
from datetime import date
from typing import Type, TypeAlias, cast
from uuid import UUID

import pytest
from gfmodules_python_shared.repository.base import RepositoryBase
from gfmodules_python_shared.schema.sql_model import TSQLModel
from sqlalchemy.orm import Session

from app.db.entities.healthcare_provider import HealthcareProvider
from app.db.entities.healthcare_provider_qualification import (
    HealthcareProviderQualification,
)
from app.db.entities.protocol import Protocol
from app.db.entities.protocol_version import ProtocolVersion
from app.db.repository.healthcare_provider_repository import (
    HealthcareProviderRepository,
)

Inserter: TypeAlias = Callable[
    [Session, Type[RepositoryBase[TSQLModel]], Iterable[TSQLModel]],
    RepositoryBase[TSQLModel],
]


@pytest.fixture
def qualification(
    protocol: Protocol,
    healthcare_provider: HealthcareProvider,
) -> HealthcareProviderQualification:
    return HealthcareProviderQualification(
        id=UUID("63c99cc8-035b-462e-aacb-be3f254637b7"),
        protocol_version=protocol.versions[0],
        healthcare_provider=healthcare_provider,
        qualification_date=date.today(),
    )


def test_get_healthcare_provider_qualifications_should_succeed(
    session: Session,
    healthcare_provider: HealthcareProvider,
    protocol: Protocol,
    protocol_version: ProtocolVersion,
    qualification: HealthcareProviderQualification,
    insert_entities: Inserter[HealthcareProvider],
) -> None:
    healthcare_provider.qualified_protocols.append(qualification)
    repository = cast(
        HealthcareProviderRepository,
        insert_entities(session, HealthcareProviderRepository, (healthcare_provider,)),
    )
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

    actual_qualified_providers = [
        row._mapping for row in (repository.get_qualified_providers())
    ]

    assert expected_qualified_providers == actual_qualified_providers


@pytest.mark.parametrize(
    "qualified, insert, kwargs",
    (
        pytest.param(
            True, True, {"limit": 2, "offset": 3}, id="if offset exceeds the result"
        ),
        pytest.param(False, True, {}, id="if no qualified healthcare provider"),
        pytest.param(False, False, {}, id="if no healthcare provider exists"),
    ),
)
def test_get_qualified_providers_should_return_empty_list(
    insert: bool,
    qualified: bool,
    kwargs: dict[str, int],
    session: Session,
    healthcare_provider: HealthcareProvider,
    insert_entities: Inserter[HealthcareProvider],
    request: pytest.FixtureRequest,
) -> None:
    if qualified:
        qualification = request.getfixturevalue("qualification")
        healthcare_provider.qualified_protocols.append(qualification)
    repository = (
        cast(
            HealthcareProviderRepository,
            insert_entities(
                session, HealthcareProviderRepository, (healthcare_provider,)
            ),
        )
        if insert
        else HealthcareProviderRepository(session)
    )
    assert not [row._mapping for row in repository.get_qualified_providers(**kwargs)]


def test_get_healthcare_provider_qualification_should_return_results_exact_as_limit_provided(
    session: Session,
    healthcare_provider: HealthcareProvider,
    protocol: Protocol,
    protocol_version: ProtocolVersion,
    qualification: HealthcareProviderQualification,
    insert_entities: Inserter,
) -> None:
    protocol_version_2 = ProtocolVersion(
        id=UUID("6590bbd3-8cb1-4bae-9443-83f1905b9499"),
        version="example 2",
    )
    protocol.versions.append(protocol_version_2)
    healthcare_provider.qualified_protocols.append(qualification)
    healthcare_provider.qualified_protocols.append(
        HealthcareProviderQualification(
            id=UUID("8caece01-90da-4941-95cc-bf7d31a90778"),
            protocol_version=protocol_version_2,
            healthcare_provider=healthcare_provider,
            qualification_date=date.today(),
        )
    )

    repository = cast(
        HealthcareProviderRepository,
        insert_entities(session, HealthcareProviderRepository, (healthcare_provider,)),
    )

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
        row._mapping for row in repository.get_qualified_providers(limit=1)
    ]

    assert expected_qualified_providers == actual_qualified_providers
    assert len(expected_qualified_providers) == len(actual_qualified_providers)
