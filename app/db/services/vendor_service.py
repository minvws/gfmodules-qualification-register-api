from gfmodules_python_shared.schema.pagination.page_schema import Page
from gfmodules_python_shared.session.session_manager import (
    get_repository,
    session_manager,
)
from uuid import UUID

from app.db.repository.vendor_repository import VendorRepository
from app.exceptions.http_base_exceptions import NotFoundException
from app.schemas.vendor.mapper import (
    map_vendor_entity_to_dto,
    map_vendor_entities_to_dtos,
)
from app.schemas.vendor.schema import VendorDto


class VendorService:
    @session_manager
    def get(
        self, id: UUID, *, vendor_repository: VendorRepository = get_repository()
    ) -> VendorDto:
        entity = vendor_repository.get(id=id)
        if entity is None:
            raise NotFoundException()
        return map_vendor_entity_to_dto(entity=entity)

    @session_manager
    def get_paginated(
        self,
        limit: int,
        offset: int,
        *,
        vendor_repository: VendorRepository = get_repository(),
    ) -> Page[VendorDto]:
        vendors = vendor_repository.get_many(limit=limit, offset=offset)
        dto = map_vendor_entities_to_dtos(entities=vendors)
        total = vendor_repository.count()

        return Page(items=dto, limit=limit, offset=offset, total=total)
