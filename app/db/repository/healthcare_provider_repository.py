import logging
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.repository.repository_base import RepositoryBase, TArgs

from app.db.entities.HealthcareProvider import HealthcareProvider

logger = logging.getLogger(__name__)


class HealthcareProviderRepository(RepositoryBase):
    def __init__(self, session: Session):
        super().__init__(session)

    def get_all(self, **kwargs: TArgs) -> Sequence[HealthcareProvider]:
        return self.session.scalars(
            select(HealthcareProvider)).all()
