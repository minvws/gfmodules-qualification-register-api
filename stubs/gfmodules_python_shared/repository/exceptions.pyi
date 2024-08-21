from sqlalchemy.exc import NoResultFound
from typing import TypeVar

T = TypeVar('T')

class EntryNotFound(NoResultFound):
    def __init__(self, model: type[T]) -> None: ...
