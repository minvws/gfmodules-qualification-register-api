import uuid
from typing import List

from gfmodules_python_shared.session.session_manager import get_repository, session_manager

from app.db.repository.vendor_repository import VendorRepository
from app.exceptions.http_base_exceptions import NotFoundException
from app.schemas.vendor.mapper import map_vendor_entity_to_dto, map_vendor_entities_to_dtos
from app.schemas.vendor.schema import VendorDto


class VendorService:

    @session_manager
    def get(
        self, id: uuid.UUID, vendor_repository: VendorRepository = get_repository()
    ) -> VendorDto:
        entity = vendor_repository.get(id=id)
        if entity is None:
            raise NotFoundException()
        return map_vendor_entity_to_dto(entity=entity)

    @session_manager
    def get_all(
        self, vendor_repository: VendorRepository = get_repository()
    ) -> List[VendorDto]:
        return map_vendor_entities_to_dtos(entities=vendor_repository.get_many())
