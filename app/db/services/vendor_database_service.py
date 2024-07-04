import uuid
from abc import abstractmethod, ABCMeta
from typing import Sequence

from app.db.repository.vendor_repository import VendorRepository
from app.db.session_manager import session_manager, repository
from app.dto.VendorDto import VendorDto
from app.exceptions.http_base_exceptions import NotFoundException
from app.mappers.mapper import Mapper


class VendorDatabaseServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def get(self, id_: uuid.UUID) -> VendorDto: ...

    @abstractmethod
    def get_all(self) -> Sequence[VendorDto]: ...


class VendorDatabaseService(VendorDatabaseServiceInterface):

    @session_manager
    def get(
        self, id: uuid.UUID, vendor_repository: VendorRepository = repository()
    ) -> VendorDto:
        entity = vendor_repository.get(id=id)
        if entity is None:
            raise NotFoundException()
        return Mapper.to_vendor_dto(entity=entity)

    @session_manager
    def get_all(
        self, vendor_repository: VendorRepository = repository()
    ) -> Sequence[VendorDto]:
        return Mapper.to_vendor_dtos(entities=vendor_repository.get_all())
