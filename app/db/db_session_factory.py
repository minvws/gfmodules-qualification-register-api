from sqlalchemy import Engine

from app.db.db_session import DbSession


class DbSessionFactory:
    def __init__(self, engine: Engine):
        self._engine = engine

    def create(self) -> DbSession:
        return DbSession(self._engine)
