from typing import List

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
    def get_all(
        self, repository: ApplicationVersionQualificationRepository = get_repository()
    ) -> List[QualifiedVendorDTO]:
        qualified_applications = repository.get_qualified_application_versions()
        return flatten_vendor_qualifications(qualified_applications)
