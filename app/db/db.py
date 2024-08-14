import logging

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from app.db.entities.base import Base

logger = logging.getLogger(__name__)


class Database:
    def __init__(self, dsn: str, pool_recycle: int = 25, pool_size: int = 10):
        try:
            self.engine = create_engine(dsn, echo=False, pool_recycle=pool_recycle, pool_size=pool_size)
        except BaseException as e:
            logger.error("Error while connecting to database: %s", e)
            raise e

    def generate_tables(self) -> None:
        logger.info("Generating tables...")
        Base.metadata.create_all(self.engine)

    def is_healthy(self) -> bool:
        """
        Check if the database is healthy

        :return: True if the database is healthy, False otherwise
        """
        try:
            with Session(self.engine) as session:
                session.execute(text('SELECT 1'))
            return True
        except Exception as e:
            logger.info("Database is not healthy: %s", e)
            return False
