from typing import cast

from sqlalchemy.orm import Session
from app.db.entities import Role
from app.db.repository import RoleRepository
from tests.utests.db.repositories.test_healthcare_provider_repository import Inserter
from tests.utests.db.utils import are_the_same_entity


def test_create_should_succeed_when_given_a_valid_role_object(
    session: Session, insert_entities: Inserter[Role], role: Role
):
    repository = cast(RoleRepository, insert_entities(session, RoleRepository, (role,)))
    assert are_the_same_entity(repository.get_or_fail(id=role.id), role)
    assert repository.count() == 1
