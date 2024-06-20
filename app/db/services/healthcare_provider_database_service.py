from typing import Sequence

from app.db.db_session_factory import DbSessionFactory
from app.db.repository.healthcare_provider_repository import HealthcareProviderRepository
from app.dto.HealthcareProviderDto import HealthcareProviderDto
from app.mappers import mapper


class HealthcareProviderDatabaseService:
    def __init__(
            self,
            db_session_factory: DbSessionFactory,
    ) -> None:
        self._db_session_factory = db_session_factory

    def get_all(self) -> Sequence[HealthcareProviderDto]:
        with self._db_session_factory.create() as session:
            healthcare_provider_repository = session.get_repository(HealthcareProviderRepository)
            return mapper.to_healthcare_provider_dtos(entities=healthcare_provider_repository.get_all())
