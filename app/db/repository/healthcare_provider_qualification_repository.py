from typing import Sequence, TYPE_CHECKING

from gfmodules_python_shared.repository.repository_base import RepositoryBase, TArgs
from gfmodules_python_shared.session.db_session import DbSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.db.entities.healthcare_provider_qualification import (
    HealthcareProviderQualification,
)
from app.db.entities.protocol_version import ProtocolVersion


class HealthcareProviderQualificationRepository(
    RepositoryBase[HealthcareProviderQualification]
):
    def __init__(self, db_session: DbSession):
        super().__init__(session=db_session, cls_model=HealthcareProviderQualification)

    def get_qualified_healthcare_providers(
        self, **kwargs: TArgs
    ) -> Sequence[HealthcareProviderQualification]:
        stmt = (
            select(HealthcareProviderQualification)
            .options(selectinload(HealthcareProviderQualification.healthcare_provider))
            .options(
                selectinload(
                    HealthcareProviderQualification.protocol_version
                ).selectinload(ProtocolVersion.protocol)
            )
            .filter_by(**kwargs)
        )
        results = self.session.scalars_all(stmt)
        if TYPE_CHECKING:
            if not isinstance(results, Sequence):
                raise TypeError(f"Unexpected result type: {type(results)}")

        return results
