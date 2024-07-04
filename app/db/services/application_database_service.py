import uuid
from abc import ABCMeta, abstractmethod
from typing import Sequence

from app.db.repository.application_repository import ApplicationRepository
from app.db.session_manager import session_manager, repository
from app.dto.ApplicationWithVendorDto import ApplicationWithVendorDto
from app.exceptions.http_base_exceptions import NotFoundException
from app.mappers.mapper import Mapper


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
        return Mapper.to_application_dto(entity=entity)

    @session_manager
    def get_all(
        self, application_repository: ApplicationRepository = repository()
    ) -> Sequence[ApplicationWithVendorDto]:
        return Mapper.to_application_dtos(entities=application_repository.get_all())
