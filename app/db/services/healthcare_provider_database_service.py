from abc import ABCMeta, abstractmethod
from typing import Sequence

from app.db.repository.healthcare_provider_repository import (
    HealthcareProviderRepository,
)
from app.db.session_manager import session_manager, repository
from app.dto.qualification_dto import QualificationDto
from app.mappers.mapper import Mapper


class HealthcareProviderDatabaseServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_all(self) -> Sequence[QualificationDto]: ...


class HealthcareProviderDatabaseService(HealthcareProviderDatabaseServiceInterface):
    @session_manager
    def get_all(
        self,
        healthcare_provider_repository: HealthcareProviderRepository = repository(),
    ) -> Sequence[QualificationDto]:
        return Mapper.to_qualification_dtos(
            entities=healthcare_provider_repository.get_all()
        )
