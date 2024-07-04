from app.db.db_session import DbSession
from app.db.entities.role import Role
from app.db.repository.repository_base import RepositoryBase


class RoleRepository(RepositoryBase[Role]):

    model = Role

    def __init__(self, db_session: DbSession):
        super().__init__(db_session)
