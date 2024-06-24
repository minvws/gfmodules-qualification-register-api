import inject
import pytest

from app.db.db_session import DbSession
from app.db.db_session_factory import DbSessionFactory, DbSessionContext
from app.db.repository_factory import RepositoryFactory


@pytest.fixture()
def db_session_mock(mocker):
    yield mocker.Mock(spec=DbSession)


@pytest.fixture()
def injector(mocker, db_session_mock):
    db_session_factory = mocker.Mock(spec=DbSessionFactory)
    db_session_context = mocker.Mock(spec=DbSessionContext)

    mocker.patch.object(db_session_factory, "create", return_value=db_session_context)
    db_session_context.__enter__ = mocker.Mock(return_value=db_session_mock)
    db_session_context.__exit__ = mocker.Mock(return_value=None)

    def injector_config(binder):
        binder.bind(DbSessionFactory, db_session_factory)
        binder.bind(RepositoryFactory, mocker.Mock())

    inject.configure(injector_config)
    yield
    inject.clear()
