from gfmodules_python_shared.schema.pagination.page_schema import Page
from gfmodules_python_shared.session.session_manager import (
    session_manager,
    get_repository,
)

from app.db.repository.application_version_qualification_repository import (
    ApplicationVersionQualificationRepository,
)
from app.schemas.vendor_qualifications.mapper import flatten_vendor_qualifications
from app.schemas.vendor_qualifications.schema import QualifiedVendorDTO


class VendorQualificationService:

    @session_manager
    def get_paginated(
        self,
        limit: int,
        offset: int,
        repository: ApplicationVersionQualificationRepository = get_repository()
    ) -> Page[QualifiedVendorDTO]:
        qualified_vendors = repository.get_many(limit=limit, offset=offset)
        dto = flatten_vendor_qualifications(qualified_vendors)
        total = repository.count()

        return Page(items=dto, limit=limit, offset=offset, total=total)
