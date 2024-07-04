from app.db.db_session import DbSession
from app.db.entities.application import Application
from app.db.repository.repository_base import RepositoryBase


class ApplicationRepository(RepositoryBase[Application]):

    model = Application

    def __init__(self, db_session: DbSession):
        super().__init__(db_session)
