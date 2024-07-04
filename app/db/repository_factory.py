from typing import Type

from sqlalchemy import Engine

from app.db.db_session import DbSession
from app.db.repository.repository_base import RepositoryBase, TRepositoryBase


class RepositoryFactory:
    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def get_repository(
        self,
        repository_class: Type[TRepositoryBase],
        db_session: DbSession,
    ) -> TRepositoryBase:
        if issubclass(repository_class, RepositoryBase):
            return repository_class(db_session)
        raise ValueError(f"No repository registered for model {repository_class}")
