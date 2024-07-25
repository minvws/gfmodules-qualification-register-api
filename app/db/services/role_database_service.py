import uuid
from abc import ABCMeta, abstractmethod
from typing import Sequence

from app.db.repository.role_repository import RoleRepository
from app.exceptions.http_base_exceptions import NotFoundException
from app.db.session_manager import session_manager, repository
from app.schemas.roles.mapper import map_role_entity_to_dto, map_role_entities_to_dtos
from app.schemas.roles.schema import RoleDto


class RoleDatabaseServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def get(self, id_: uuid.UUID) -> RoleDto: ...

    @abstractmethod
    def get_all(self) -> Sequence[RoleDto]: ...


class RoleDatabaseService(RoleDatabaseServiceInterface):
    @session_manager
    def get(
        self, id_: uuid.UUID, role_repository: RoleRepository = repository()
    ) -> RoleDto:
        entity = role_repository.get(id=id_)
        if entity is None:
            raise NotFoundException()
        return map_role_entity_to_dto(entity=entity)

    @session_manager
    def get_all(
        self, role_repository: RoleRepository = repository()
    ) -> Sequence[RoleDto]:
        return map_role_entities_to_dtos(entities=role_repository.get_all())
