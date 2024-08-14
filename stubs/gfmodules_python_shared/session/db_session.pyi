from _typeshed import Incomplete
from sqlalchemy import Engine as Engine, Select as Select
from typing import Any, Sequence, TypeVar

T = TypeVar('T')

class DbSession:
    session: Incomplete
    def __init__(self, engine: Engine) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def merge(self, entity: T) -> T: ...
    def create(self, entity: T) -> None: ...
    def update(self, entity: T) -> None: ...
    def delete(self, entity: T) -> None: ...
    def scalars_first(self, statement: Select[tuple[T]]) -> T | None: ...
    def scalars_all(self, statement: Select[tuple[T]]) -> Sequence[T]: ...
    def execute_scalar(self, statement: Select[tuple[T]]) -> Any | None: ...