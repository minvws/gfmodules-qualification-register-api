import uuid

import inject
import pytest

from app.db.entities.system_type import SystemType
from app.db.repository_factory import RepositoryFactory
from app.db.services.system_type_database_service import SystemTypeDatabaseService
from app.schemas.system_type.schema import SystemTypeDto


@pytest.fixture()
def system_type_repository(mocker):
    system_type_repository = mocker.Mock()
    mocker.patch.object(
        inject.instance(RepositoryFactory),
        "get_repository",
        return_value=system_type_repository,
    )
    yield system_type_repository


def test_get(injector, mocker, system_type_repository):
    uuid_ = uuid.uuid4()
    system_type = SystemType(id=uuid_, name="System Type A", description=None)
    expected = SystemTypeDto(id=uuid_, name="System Type A", description=None)

    mocker.patch.object(system_type_repository, "get", return_value=system_type)

    service = SystemTypeDatabaseService()
    actual = service.get(uuid_)

    assert actual == expected


def test_get_all(injector, mocker, system_type_repository):
    uuid_ = uuid.uuid4()
    system_types = [SystemType(id=uuid_, name="System Type A", description=None)]
    expected = [SystemTypeDto(id=uuid_, name="System Type A", description=None)]

    mocker.patch.object(system_type_repository, "get_all", return_value=system_types)

    service = SystemTypeDatabaseService()
    actual = service.get_all()

    assert actual == expected
