import inspect
import inject

from typing import Callable, TypeVar, ParamSpec, Any

from app.db.db_session_factory import DbSessionFactory
from app.db.repository.repository_base import RepositoryBase
from app.db.repository_factory import RepositoryFactory


T = TypeVar("T")
P = ParamSpec("P")


def repository() -> Any:
    return None


def session_manager(func: Callable[P, T]) -> Callable[P, T]:
    def wrapper(self: ParamSpec, *args: P.args, **kwargs: P.kwargs) -> T:
        signature = inspect.signature(func)

        db_session_factory = inject.instance(DbSessionFactory)
        repository_factory = inject.instance(RepositoryFactory)

        func_args: P.args = {}

        params_list = [p for p in signature.parameters.values() if p.name != "self"]
        for arg, param in zip(args, params_list[: len(args)]):
            func_args[param.name] = arg

        with db_session_factory.create() as session:
            for p in signature.parameters.values():
                # copy self param to func_args if present
                if p.name == "self":
                    func_args[p.name] = self
                    continue

                # Ignore param if already in kwargs
                if p.name in kwargs:
                    func_args[p.name] = kwargs[p.name]
                    continue

                # Ignore param if already handled in args
                if p.name in func_args:
                    continue

                # Copy supplied None value to func_args
                if p.annotation is inspect.Parameter.empty:
                    func_args[p.name] = None
                    continue

                # Ignore anything that is not a repositoryBase
                if not issubclass(p.annotation, RepositoryBase):
                    continue
                func_args[p.name] = repository_factory.get_repository(
                    p.annotation, session
                )

            # Handle actual function inside session context
            return func(**func_args)

    return wrapper  # type: ignore
