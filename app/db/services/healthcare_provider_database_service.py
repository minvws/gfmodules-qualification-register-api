from typing import Sequence

from gfmodules_python_shared.session.session_manager import get_repository, session_manager
from app.db.repository.healthcare_provider_repository import (
    HealthcareProviderRepository,
)
from app.schemas.qualification.mapper import map_healthcare_provider_entities_to_qualification_dtos
from app.schemas.qualification.schema import QualificationDto


class HealthcareProviderDatabaseService:
    @session_manager
    def get_all(
        self,
        healthcare_provider_repository: HealthcareProviderRepository = get_repository(),
    ) -> Sequence[QualificationDto]:
        return map_healthcare_provider_entities_to_qualification_dtos(
            entities=healthcare_provider_repository.get_all()
        )
