from gfmodules_python_shared.schema.pagination.page_schema import Page
from gfmodules_python_shared.session.session_manager import (
    get_repository,
    session_manager,
)

from app.db.repository.healthcare_provider_qualification_repository import (
    HealthcareProviderQualificationRepository,
)
from app.db.repository.healthcare_provider_repository import (
    HealthcareProviderRepository,
)
from app.schemas.healthcare_provider_qualification.mapper import (
    flatten_healthcare_provider_qualification,
)
from app.schemas.healthcare_provider_qualification.schema import (
    QualifiedHealthcareProviderDTO,
)
from app.schemas.qualification.mapper import (
    map_healthcare_provider_entities_to_qualification_dtos,
)
from app.schemas.qualification.schema import QualificationDto


class HealthcareProviderService:

    @session_manager
    def get_paginated(
        self,
        limit: int,
        offset: int,
        healthcare_provider_repository: HealthcareProviderRepository = get_repository(),
    ) -> Page[QualificationDto]:
        healthcare_providers = healthcare_provider_repository.get_many(
            limit=limit, offset=offset
        )
        dto = map_healthcare_provider_entities_to_qualification_dtos(
            entities=healthcare_providers
        )
        total = healthcare_provider_repository.count()

        return Page(items=dto, limit=limit, offset=offset, total=total)

    @session_manager
    def get_qualified_healthcare_providers(
        self,
        limit: int,
        offset: int,
        healthcare_providers_qualification_repository: HealthcareProviderQualificationRepository = get_repository(),
    ) -> Page[QualifiedHealthcareProviderDTO]:
        qualified_providers = (
            healthcare_providers_qualification_repository.get_qualified_healthcare_providers()
        )
        dto = flatten_healthcare_provider_qualification(qualified_providers)
        total = healthcare_providers_qualification_repository.count()

        return Page(items=dto, total=total, limit=limit, offset=offset)
