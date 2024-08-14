from typing import List

from gfmodules_python_shared.session.session_manager import session_manager, get_repository
from uuid import UUID

from app.db.repository.role_repository import RoleRepository
from app.exceptions.http_base_exceptions import NotFoundException
from app.schemas.roles.mapper import map_role_entity_to_dto, map_role_entities_to_dtos
from app.schemas.roles.schema import RoleDto


class RoleService:
    @session_manager
    def get(
        self, id_: UUID, role_repository: RoleRepository = get_repository()
    ) -> RoleDto:
        entity = role_repository.get(id=id_)
        if entity is None:
            raise NotFoundException()
        return map_role_entity_to_dto(entity=entity)

    @session_manager
    def get_all(
        self, role_repository: RoleRepository = get_repository()
    ) -> List[RoleDto]:
        return map_role_entities_to_dtos(entities=role_repository.get_many())
