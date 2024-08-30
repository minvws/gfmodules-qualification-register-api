from typing import TypeVar, Any

from gfmodules_python_shared.repository.repository_base import RepositoryBase
from gfmodules_python_shared.session.db_session import DbSession
from sqlalchemy import func, Result, select, Select

from app.db.entities.healthcare_provider import HealthcareProvider
from app.db.entities.healthcare_provider_qualification import (
    HealthcareProviderQualification,
)
from app.db.entities.protocol import Protocol
from app.db.entities.protocol_version import ProtocolVersion

_T = TypeVar("_T", bound=tuple[Any, ...])


class HealthcareProviderRepository(RepositoryBase[HealthcareProvider]):

    def __init__(self, db_session: DbSession):
        super().__init__(session=db_session, cls_model=HealthcareProvider)

    def _apply_join(self, stmt: Select[_T]) -> Select[_T]:
        return (
            stmt.outerjoin(HealthcareProviderQualification.healthcare_provider)
            .outerjoin(HealthcareProviderQualification.protocol_version)
            .outerjoin(ProtocolVersion.protocol)
        )

    def get_qualified_providers(
        self, limit: int | None = None, offset: int | None = None
    ) -> Result[Any]:
        select_stmt = select(
            HealthcareProviderQualification.id.label("qualification_id"),
            HealthcareProviderQualification.qualification_date,
            HealthcareProvider.id.label("healthcare_provider_id"),
            HealthcareProvider.statutory_name.label("healthcare_provider"),
            ProtocolVersion.id.label("protocol_version_id"),
            ProtocolVersion.version.label("protocol_version"),
            Protocol.id.label("protocol_id"),
            Protocol.name.label("protocol"),
            Protocol.protocol_type,
        )
        results = self.session.session.execute(
            self._apply_join(select_stmt).limit(limit).offset(offset)
        )

        return results

    def get_total_qualified_providers(self) -> int:
        select_stmt = select(func.count())
        results = self.session.session.execute(self._apply_join(select_stmt)).scalar()
        if results is None:
            return 0

        return results
