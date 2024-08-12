from abc import ABCMeta, abstractmethod
from typing import Sequence

from app.db.repository.healthcare_provider_repository import (
    HealthcareProviderRepository,
)
from app.db.session_manager import session_manager, repository
from app.schemas.qualification.mapper import map_healthcare_provider_entities_to_qualification_dtos
from app.schemas.qualification.schema import QualificationDto


class HealthcareProviderDatabaseServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_all(self) -> Sequence[QualificationDto]: ...


class HealthcareProviderDatabaseService(HealthcareProviderDatabaseServiceInterface):
    @session_manager
    def get_all(
        self,
        healthcare_provider_repository: HealthcareProviderRepository = repository(),
    ) -> Sequence[QualificationDto]:
        return map_healthcare_provider_entities_to_qualification_dtos(
            entities=healthcare_provider_repository.get_all()
        )
