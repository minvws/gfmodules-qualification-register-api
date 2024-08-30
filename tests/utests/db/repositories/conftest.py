from typing import Generator, Any

import pytest
from gfmodules_python_shared.session.db_session import DbSession
from gfmodules_python_shared.session.session_factory import DbSessionFactory

from app.db.db import Database
from app.db.repository.healthcare_provider_repository import (
    HealthcareProviderRepository,
)
from app.db.repository.protocol_repository import ProtocolRepository
from app.db.repository.role_repository import RoleRepository


@pytest.fixture()
def session() -> Generator[DbSession, Any, None]:
    db = Database("sqlite:///:memory:")
    db.generate_tables()
    session_factory = DbSessionFactory(db.engine)
    session = session_factory.create()

    yield session


@pytest.fixture()
def role_repository(session: DbSession) -> RoleRepository:
    yield RoleRepository(db_session=session)


@pytest.fixture()
def healthcare_provider_repository(session: DbSession) -> HealthcareProviderRepository:
    yield HealthcareProviderRepository(db_session=session)


@pytest.fixture()
def protocol_repository(session: DbSession) -> ProtocolRepository:
    yield ProtocolRepository(db_session=session)
