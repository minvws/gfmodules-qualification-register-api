from typing import Any, TypeVar

from gfmodules_python_shared.repository.base import RepositoryBase
from sqlalchemy import ColumnExpressionArgument, Result, Select, func, select

from app.db.entities import (
    HealthcareProvider,
    HealthcareProviderQualification,
    Protocol,
    ProtocolVersion,
)

_T = TypeVar("_T", bound=tuple[Any, ...])


class HealthcareProviderRepository(RepositoryBase[HealthcareProvider]):
    @property
    def order_by(self) -> tuple[ColumnExpressionArgument[Any] | str, ...]:
        return (HealthcareProvider.created_at.desc(),)

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
        return self.session.execute(
            self._apply_join(select_stmt).limit(limit).offset(offset)
        )

    def get_total_qualified_providers(self) -> int:
        select_stmt = select(func.count())
        return self.session.execute(self._apply_join(select_stmt)).scalar() or 0
