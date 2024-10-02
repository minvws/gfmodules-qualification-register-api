from gfmodules_python_shared.schema.pagination.page_schema import Page
from gfmodules_python_shared.session.session_manager import (
    get_repository,
    session_manager,
)
from uuid import UUID

from app.db.repository.healthcare_provider_repository import (
    HealthcareProviderRepository,
)
from app.exceptions.http_base_exceptions import NotFoundException
from app.schemas.healthcare_provider.mapper import map_healthcare_provider_entity_to_dto
from app.schemas.healthcare_provider.schema import HealthcareProviderDto
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
        *,
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
    def get(
        self,
        provider_id: UUID,
        *,
        healthcare_provider_repository: HealthcareProviderRepository = get_repository(),
    ) -> HealthcareProviderDto:
        db_provider = healthcare_provider_repository.get(id=provider_id)
        if db_provider is None:
            raise NotFoundException()

        return map_healthcare_provider_entity_to_dto(entity=db_provider)

    @session_manager
    def get_qualified_healthcare_providers(
        self,
        limit: int,
        offset: int,
        *,
        healthcare_providers_repository: HealthcareProviderRepository = get_repository(),
    ) -> Page[QualifiedHealthcareProviderDTO]:
        db_rows = healthcare_providers_repository.get_qualified_providers(
            limit=limit, offset=offset
        )
        dto = [QualifiedHealthcareProviderDTO(**row._mapping) for row in db_rows]
        total = healthcare_providers_repository.get_total_qualified_providers()
        return Page(items=dto, limit=limit, offset=offset, total=total)
