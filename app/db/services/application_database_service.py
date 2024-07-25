import uuid
from abc import ABCMeta, abstractmethod
from typing import Sequence

from app.db.repository.application_repository import ApplicationRepository
from app.db.session_manager import session_manager, repository
from app.exceptions.http_base_exceptions import NotFoundException
from app.schemas.application.mapper import (
    map_application_entity_to_dto,
    map_application_entities_to_dtos
)
from app.schemas.application.schema import ApplicationWithVendorDto


class ApplicationDatabaseServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def get(
        self,
        id_: uuid.UUID,
        application_repository: ApplicationRepository = repository(),
    ) -> ApplicationWithVendorDto: ...

    @abstractmethod
    def get_all(
        self,
        application_repository: ApplicationRepository = repository(),
    ) -> Sequence[ApplicationWithVendorDto]: ...


class ApplicationDatabaseService(ApplicationDatabaseServiceInterface):
    @session_manager
    def get(
        self,
        id: uuid.UUID,
        application_repository: ApplicationRepository = repository(),
    ) -> ApplicationWithVendorDto:
        entity = application_repository.get(id=id)
        if entity is None:
            raise NotFoundException()
        return map_application_entity_to_dto(entity=entity)

    @session_manager
    def get_all(
        self, application_repository: ApplicationRepository = repository()
    ) -> Sequence[ApplicationWithVendorDto]:
        return map_application_entities_to_dtos(entities=application_repository.get_all())
