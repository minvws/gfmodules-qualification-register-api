import uuid
from typing import List

from gfmodules_python_shared.session.session_manager import session_manager, get_repository

from app.db.repository.system_type_repository import SystemTypeRepository
from app.exceptions.http_base_exceptions import NotFoundException
from app.schemas.system_type.mapper import map_system_type_entities_to_dtos, map_system_type_entity_to_dto
from app.schemas.system_type.schema import SystemTypeDto


class SystemTypeService:
    @session_manager
    def get(
        self, id: uuid.UUID, system_type_repository: SystemTypeRepository = get_repository()
    ) -> SystemTypeDto:
        entity = system_type_repository.get(id=id)
        if entity is None:
            raise NotFoundException()
        return map_system_type_entity_to_dto(entity=entity)

    @session_manager
    def get_all(
        self, system_type_repository: SystemTypeRepository = get_repository()
    ) -> List[SystemTypeDto]:
        return map_system_type_entities_to_dtos(entities=system_type_repository.get_many())
