from gfmodules_python_shared.schema.pagination.page_schema import Page
from gfmodules_python_shared.session.session_manager import (
    session_manager,
    get_repository,
)

from app.db.repository.vendor_repository import VendorRepository
from app.schemas.vendor_qualifications.schema import QualifiedVendorDTO


class VendorQualificationService:
    @session_manager
    def get_paginated(
        self,
        limit: int,
        offset: int,
        *,
        repository: VendorRepository = get_repository(),
    ) -> Page[QualifiedVendorDTO]:
        db_rows = repository.get_qualified_vendors(limit=limit, offset=offset)
        dto = [QualifiedVendorDTO(**row._mapping) for row in db_rows]
        count = repository.total_qualified_vendors()

        return Page(
            items=dto,
            limit=limit,
            offset=offset,
            total=count,
        )
