from typing import Sequence

from app.db.entities.role import Role
from app.schemas.roles.schema import RoleDto


def map_role_entities_to_dtos(entities: Sequence[Role]) -> Sequence[RoleDto]:
    return [map_role_entity_to_dto(role) for role in entities]


def map_role_entity_to_dto(entity: Role) -> RoleDto:
    return RoleDto(id=entity.id, name=entity.name, description=entity.description)
