from collections.abc import Iterator

import pytest
from inject import configure, instance
from sqlalchemy.orm import Session, sessionmaker

from app.db.repository import (
    HealthcareProviderRepository,
    ProtocolRepository,
    RoleRepository,
)
from tests.utests.db.utils import container_config


@pytest.fixture(scope="module", autouse=True)
def with_container() -> None:
    configure(container_config)


@pytest.fixture(scope="module")
def session_maker() -> sessionmaker[Session]:
    return instance(sessionmaker[Session])


@pytest.fixture
def session(session_maker: sessionmaker[Session]) -> Iterator[Session]:
    with session_maker() as session:
        yield session


@pytest.fixture()
def role_repository(session: Session) -> RoleRepository:
    return RoleRepository(session)


@pytest.fixture()
def healthcare_provider_repository(session: Session) -> HealthcareProviderRepository:
    return HealthcareProviderRepository(session)


@pytest.fixture()
def protocol_repository(session: Session) -> ProtocolRepository:
    return ProtocolRepository(session)
