import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from gfmodules_python_shared.repository.exceptions import EntryNotFound as EntryNotFound
from gfmodules_python_shared.session.db_session import DbSession as DbSession
from gfmodules_python_shared.utils.validators import validate_sets_equal as validate_sets_equal
from sqlalchemy.orm import DeclarativeBase
from typing import Dict, Generic, List, Sequence, Type, TypeVar
from uuid import UUID

T = TypeVar('T', bound=DeclarativeBase)
TArgs = TypeVar('TArgs', bound=str | UUID | Dict[str, str])

class GenericRepository(ABC, Generic[T], metaclass=abc.ABCMeta):
    session: Incomplete
    def __init__(self, session: DbSession) -> None: ...
    @abstractmethod
    def create(self, entity: T) -> None: ...
    @abstractmethod
    def update(self, entity: T) -> None: ...
    @abstractmethod
    def delete(self, entity: T) -> None: ...
    @abstractmethod
    def get(self, **kwargs: TArgs) -> T | None: ...

class RepositoryBase(GenericRepository[T], ABC):
    model: Incomplete
    def __init__(self, session: DbSession, cls_model: Type[T]) -> None: ...
    def create(self, entity: T) -> None: ...
    def update(self, entity: T) -> None: ...
    def delete(self, entity: T) -> None: ...
    def get(self, **kwargs: TArgs) -> T | None: ...
    def get_or_fail(self, **kwargs: TArgs) -> T: ...
    def get_many(self, limit: int | None = None, offset: int | None = None, **kwargs: TArgs) -> Sequence[T]: ...
    def count(self, **kwargs: TArgs) -> int: ...
    def get_by_property(self, attribute: str, values: List[str]) -> Sequence[T]: ...
    def get_by_property_exact(self, attribute: str, values: List[str]) -> Sequence[T]: ...