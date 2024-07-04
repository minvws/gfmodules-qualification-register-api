from unittest.mock import Mock

import inject

from app.db.repository.role_repository import RoleRepository
from app.db.repository.system_type_repository import SystemTypeRepository
from app.db.repository_factory import RepositoryFactory
from app.db.session_manager import session_manager


def test_session_manager(injector, db_session_mock, mocker) -> None:
    repository_factory = inject.instance(RepositoryFactory)
    repository_factory.get_repository.return_value = Mock(RoleRepository)

    class Clazz:
        called = False

        @session_manager
        def to_be_decorated(
            self,
            a: str,
            b: str,
            role_repository: RoleRepository,
            *,
            c: int = 0,
            d: int = 0,
            system_type_repository: SystemTypeRepository
        ):
            assert isinstance(role_repository, RoleRepository)
            assert isinstance(system_type_repository, SystemTypeRepository)
            assert a == "a"
            assert b == "b"
            assert c == 5
            assert d == 0
            self.called = True

    clazz = Clazz()
    clazz.to_be_decorated(
        "a", b="b", c=5, system_type_repository=Mock(SystemTypeRepository)
    )

    repository_factory.get_repository.assert_called_with(
        RoleRepository, db_session_mock
    )

    assert clazz.called
