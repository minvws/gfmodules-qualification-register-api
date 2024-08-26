from gfmodules_python_shared.repository.repository_base import RepositoryBase
from gfmodules_python_shared.session.db_session import DbSession

from app.db.entities.application_version_qualification import (
    ApplicationVersionQualification,
)


class ApplicationVersionQualificationRepository(
    RepositoryBase[ApplicationVersionQualification]
):
    def __init__(self, db_session: DbSession):
        super().__init__(session=db_session, cls_model=ApplicationVersionQualification)
