from app.db.db_session import DbSession
from app.db.entities.healthcare_provider import HealthcareProvider
from app.db.repository.repository_base import RepositoryBase


class HealthcareProviderRepository(RepositoryBase[HealthcareProvider]):

    model = HealthcareProvider

    def __init__(self, db_session: DbSession):
        super().__init__(db_session)
