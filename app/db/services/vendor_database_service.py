import uuid
from abc import abstractmethod, ABCMeta
from typing import Sequence

from app.db.repository.vendor_repository import VendorRepository
from app.db.session_manager import session_manager, repository
from app.exceptions.http_base_exceptions import NotFoundException
from app.schemas.vendor.mapper import map_vendor_entity_to_dto, map_vendor_entities_to_dtos
from app.schemas.vendor.schema import VendorDto


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
        return map_vendor_entity_to_dto(entity=entity)

    @session_manager
    def get_all(
        self, vendor_repository: VendorRepository = repository()
    ) -> Sequence[VendorDto]:
        return map_vendor_entities_to_dtos(entities=vendor_repository.get_all())
