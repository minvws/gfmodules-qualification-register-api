import uuid

import inject
import pytest
from gfmodules_python_shared.repository.repository_factory import RepositoryFactory

from app.db.entities.role import Role
from app.db.services.role_database_service import RoleDatabaseService
from app.schemas.roles.schema import RoleDto


@pytest.fixture()
def role_repository(mocker):
    role_repository = mocker.Mock()
    mocker.patch.object(
        inject.instance(RepositoryFactory),
        "get_repository",
        return_value=role_repository,
    )
    yield role_repository


def test_get(injector, mocker, role_repository):
    uuid_ = uuid.uuid4()
    role = Role(id=uuid_, name="aRole")
    expected = RoleDto(id=uuid_, name="aRole", description=None)

    mocker.patch.object(role_repository, "get", return_value=role)

    service = RoleDatabaseService()
    actual = service.get(uuid_)

    assert actual == expected


def test_get_all(injector, mocker, role_repository):
    uuid_ = uuid.uuid4()
    roles = [Role(id=uuid_, name="aRole")]
    expected = [RoleDto(id=uuid_, name="aRole", description=None)]

    mocker.patch.object(role_repository, "get_all", return_value=roles)

    service = RoleDatabaseService()
    actual = service.get_all()

    assert actual == expected
