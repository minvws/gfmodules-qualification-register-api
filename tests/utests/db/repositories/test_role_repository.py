import pytest

from app.db.entities.role import Role
from app.db.repository.role_repository import RoleRepository


@pytest.fixture()
def mock_role() -> Role:
    return Role(
        name="aRole",
        description=None
    )


class TestRoleRepository:

    def test_create_should_succeed_when_given_a_valid_role_object(self, role_repository: RoleRepository,
                                                                  mock_role: Role):
        expected_role = mock_role

        role_repository.create(mock_role)
        actual_role = role_repository.get(id=mock_role.id)

        assert actual_role == expected_role
        assert role_repository.count() == 1
