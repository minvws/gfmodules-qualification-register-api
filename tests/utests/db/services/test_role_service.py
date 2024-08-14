from uuid import uuid4

from app.db.entities.role import Role
from app.schemas.roles.schema import RoleDto


class TestRoleService:

    def test_get(self, role_service, role_repository):
        uuid_ = uuid4()
        role = Role(id=uuid_, name="aRole", description=None)
        expected_dto = RoleDto(id=uuid_, name="aRole", description=None)

        role_repository.create(role)

        actual = role_service.get(role.id)

        assert actual == expected_dto

    def test_get_all(self, role_service, role_repository):
        uuid_ = uuid4()
        role = Role(id=uuid_, name="aRole")

        role_repository.create(role)

        expected = [RoleDto(id=uuid_, name="aRole", description=None)]

        actual = role_service.get_all()

        assert actual == expected
