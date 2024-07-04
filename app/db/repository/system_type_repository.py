from app.db.db_session import DbSession
from app.db.entities.system_type import SystemType
from app.db.repository.repository_base import RepositoryBase


class SystemTypeRepository(RepositoryBase[SystemType]):

    model = SystemType

    def __init__(self, db_session: DbSession):
        super().__init__(db_session)
