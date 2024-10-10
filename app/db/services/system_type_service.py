from gfmodules_python_shared.schema.pagination.page_schema import Page
from gfmodules_python_shared.session.session_manager import (
    session_manager,
    get_repository,
)
from uuid import UUID

from app.db.repository.system_type_repository import SystemTypeRepository
from app.exceptions.http_base_exceptions import NotFoundException
from app.schemas.system_type.mapper import (
    map_system_type_entities_to_dtos,
    map_system_type_entity_to_dto,
)
from app.schemas.system_type.schema import SystemTypeDto


class SystemTypeService:
    @session_manager
    def get(
        self,
        id: UUID,
        *,
        system_type_repository: SystemTypeRepository = get_repository(),
    ) -> SystemTypeDto:
        entity = system_type_repository.get(id=id)
        if entity is None:
            raise NotFoundException()
        return map_system_type_entity_to_dto(entity=entity)

    @session_manager
    def get_paginated(
        self,
        limit: int,
        offset: int,
        *,
        system_type_repository: SystemTypeRepository = get_repository(),
    ) -> Page[SystemTypeDto]:
        system_types = system_type_repository.get_many(limit=limit, offset=offset)
        dto = map_system_type_entities_to_dtos(entities=system_types)
        total = system_type_repository.count()

        return Page(items=dto, limit=limit, offset=offset, total=total)
