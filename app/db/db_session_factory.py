from traceback import TracebackException
from types import TracebackType

from sqlalchemy import Engine

from app.db.db_session import DbSession


class DbSessionContext:
    _db_session: DbSession | None = None

    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def __enter__(self) -> DbSession:
        self._db_session = DbSession(self._engine)
        self._db_session.open()
        return self._db_session

    def __exit__(
        self, exc_type: Exception, exc_val: TracebackException, exc_tb: TracebackType
    ) -> None:
        if self._db_session is not None:
            if exc_val is not None:
                self._db_session.rollback()
            self._db_session.close()


class DbSessionFactory:
    def __init__(self, engine: Engine):
        self._engine = engine

    def create(self) -> DbSessionContext:
        return DbSessionContext(self._engine)
