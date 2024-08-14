from gfmodules_python_shared.repository.repository_base import RepositoryBase
from gfmodules_python_shared.session.db_session import DbSession

from app.db.entities.system_type import SystemType


class SystemTypeRepository(RepositoryBase[SystemType]):

    def __init__(self, db_session: DbSession):
        super().__init__(session=db_session, cls_model=SystemType)
