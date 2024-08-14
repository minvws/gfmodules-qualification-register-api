from typing import List

from gfmodules_python_shared.session.session_manager import (
    session_manager,
    get_repository,
)
from uuid import UUID

from app.db.repository.application_repository import ApplicationRepository
from app.exceptions.http_base_exceptions import NotFoundException
from app.schemas.application.mapper import (
    map_application_entity_to_dto,
    map_application_entities_to_dtos
)
from app.schemas.application.schema import ApplicationWithVendorDto


class ApplicationService:
    @session_manager
    def get(
        self,
        id: UUID,
        application_repository: ApplicationRepository = get_repository(),
    ) -> ApplicationWithVendorDto:
        entity = application_repository.get(id=id)
        if entity is None:
            raise NotFoundException()
        return map_application_entity_to_dto(entity=entity)

    @session_manager
    def get_all(
        self, application_repository: ApplicationRepository = get_repository()
    ) -> List[ApplicationWithVendorDto]:
        return map_application_entities_to_dtos(entities=application_repository.get_many())
