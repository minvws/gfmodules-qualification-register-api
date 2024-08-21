from gfmodules_python_shared.repository.repository_base import GenericRepository as GenericRepository
from gfmodules_python_shared.session.db_session import DbSession as DbSession
from sqlalchemy.orm import DeclarativeBase as DeclarativeBase

class RepositoryFactory:
    @staticmethod
    def create(repo_class: type[GenericRepository[DeclarativeBase]], session: DbSession) -> GenericRepository[DeclarativeBase]: ...
