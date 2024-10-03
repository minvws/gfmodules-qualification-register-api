from collections.abc import Callable, Iterable, Iterator
from typing import Type
from uuid import UUID

from gfmodules_python_shared.repository.base import GenericRepository
from gfmodules_python_shared.schema.sql_model import TSQLModel
import pytest
from inject import configure, instance
from sqlalchemy.orm import Session, sessionmaker

from app.db.entities import HealthcareProvider, Protocol, ProtocolVersion, Role
from app.db.repository import (
    HealthcareProviderRepository,
    ProtocolRepository,
    RoleRepository,
)
from tests.utests.db.utils import container_config


@pytest.fixture(autouse=True)
def with_container() -> None:
    configure(container_config, clear=True)


@pytest.fixture
def session_maker() -> sessionmaker[Session]:
    return instance(sessionmaker[Session])


@pytest.fixture
def session(session_maker: sessionmaker[Session]) -> Iterator[Session]:
    with session_maker() as session:
        yield session


@pytest.fixture(scope="session")
def insert_entities() -> (
    Callable[
        [Session, Type[GenericRepository[TSQLModel]], Iterable[TSQLModel]],
        GenericRepository[TSQLModel],
    ]
):
    def inserter(
        session: Session,
        repository_type: Type[GenericRepository[TSQLModel]],
        entities: Iterable[TSQLModel],
    ) -> GenericRepository[TSQLModel]:
        repository = repository_type(session)
        with session.begin():
            for entity in entities:
                if repository.get(id=entity.id) is None:  # type: ignore
                    repository.create(entity)
        return repository

    return inserter


@pytest.fixture
def role() -> Role:
    return Role(id=UUID("f976261a-22ed-48de-b1b7-7662e12fbdc9"), name="example")


@pytest.fixture
def protocol_version() -> ProtocolVersion:
    return ProtocolVersion(
        id=UUID("8c6513af-a2cc-40a6-9d49-87602d3f2d16"), version="example"
    )


@pytest.fixture
def protocol(protocol_version: ProtocolVersion) -> Protocol:
    return Protocol(
        id=UUID("4a3a2add-49be-49a1-9284-67af5db0897b"),
        protocol_type="InformationStandard",
        name="example",
        versions=[protocol_version],
    )


@pytest.fixture
def healthcare_provider() -> HealthcareProvider:
    return HealthcareProvider(
        id=UUID("ceed25d1-d9df-4a74-883b-2e9ab3caa61a"),
        ura_code="example",
        agb_code="example",
        trade_name="example",
        statutory_name="example",
    )
