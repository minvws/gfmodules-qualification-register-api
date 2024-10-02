from uuid import UUID

from app.db.entities import Role
from app.db.repository import RoleRepository
from tests.utests.db.utils import are_the_same_entity


def test_create_should_succeed_when_given_a_valid_role_object(
    role_repository: RoleRepository,
):
    role = Role(
        id=UUID("4d5ff2af-1bcb-40d6-a53c-2c9ce4d4e470"), name="aRole", description=None
    )
    role_repository.create(role)

    assert are_the_same_entity(role_repository.get_or_fail(id=role.id), role)
    assert role_repository.count() == 1
