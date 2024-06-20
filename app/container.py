import inject

from app.db.db_session_factory import DbSessionFactory
from app.db.services.healthcare_provider_database_service import HealthcareProviderDatabaseService
from db.db import Database
from config import get_config

def container_config(binder: inject.Binder) -> None:
    config = get_config()

    db = Database(dsn=config.database.dsn)
    binder.bind(Database, db)

    db_session_factory = DbSessionFactory(db.engine)

    healthcare_provider_database_service = HealthcareProviderDatabaseService(db_session_factory)
    binder.bind(HealthcareProviderDatabaseService, healthcare_provider_database_service)


def get_database() -> Database:
    return inject.instance(Database)


def get_healthcare_provider_database_service() -> HealthcareProviderDatabaseService:
    return inject.instance(HealthcareProviderDatabaseService)


if not inject.is_configured():
    inject.configure(container_config)
