from gfmodules_python_shared.repository.repository_base import RepositoryBase
from gfmodules_python_shared.session.db_session import DbSession

from app.db.entities.healthcare_provider import HealthcareProvider


class HealthcareProviderRepository(RepositoryBase[HealthcareProvider]):

    def __init__(self, db_session: DbSession):
        super().__init__(session=db_session, cls_model=HealthcareProvider)
