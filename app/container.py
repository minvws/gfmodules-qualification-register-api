import inject

from app.db.HealthcareProviderDatabaseService import HealthcareProviderDatabaseService
from db.db import Database
from config import get_config

def container_config(binder: inject.Binder) -> None:
    config = get_config()

    db = Database(dsn=config.database.dsn)
    binder.bind(Database, db)

    healthcare_provider_database_service = HealthcareProviderDatabaseService()
    binder.bind(HealthcareProviderDatabaseService, healthcare_provider_database_service)


def get_database() -> Database:
    return inject.instance(Database)


def get_healthcare_provider_database_service() -> HealthcareProviderDatabaseService:
    return inject.instance(HealthcareProviderDatabaseService)

if not inject.is_configured():
    inject.configure(container_config)
