import uuid
from abc import ABCMeta, abstractmethod
from typing import Sequence

from app.db.repository.system_type_repository import SystemTypeRepository
from app.db.session_manager import session_manager, repository
from app.exceptions.http_base_exceptions import NotFoundException
from app.schemas.system_type.mapper import map_system_type_entities_to_dtos, map_system_type_entity_to_dto
from app.schemas.system_type.schema import SystemTypeDto


class SystemTypeDatabaseServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def get(self, id_: uuid.UUID) -> SystemTypeDto: ...

    @abstractmethod
    def get_all(self) -> Sequence[SystemTypeDto]: ...


class SystemTypeDatabaseService(SystemTypeDatabaseServiceInterface):
    @session_manager
    def get(
        self, id: uuid.UUID, system_type_repository: SystemTypeRepository = repository()
    ) -> SystemTypeDto:
        entity = system_type_repository.get(id=id)
        if entity is None:
            raise NotFoundException()
        return map_system_type_entity_to_dto(entity=entity)

    @session_manager
    def get_all(
        self, system_type_repository: SystemTypeRepository = repository()
    ) -> Sequence[SystemTypeDto]:
        return map_system_type_entities_to_dtos(entities=system_type_repository.get_all())
