from typing import Any

from gfmodules_python_shared.repository.base import RepositoryBase
from sqlalchemy import ColumnExpressionArgument, Result, func, select

from app.db.entities import (
    Vendor,
    Application,
    ApplicationVersion,
    ApplicationVersionQualification,
    ApplicationRole,
    ApplicationType,
    SystemType,
    Protocol,
    Role,
    ProtocolVersion,
)


class VendorRepository(RepositoryBase[Vendor]):
    @property
    def order_by(self) -> tuple[ColumnExpressionArgument[Any] | str, ...]:
        return (Vendor.created_at.desc(),)

    def get_qualified_vendors(
        self, limit: int | None = None, offset: int | None = None
    ) -> Result[Any]:
        stmt = (
            select(
                ApplicationVersionQualification.id.label("qualification_id"),
                ApplicationVersion.id.label("application_version_id"),
                ApplicationVersion.version.label("application_version"),
                Application.id.label("application_id"),
                Application.name.label("application"),
                SystemType.id.label("system_type_id"),
                SystemType.name.label("system_type"),
                Role.id.label("role_id"),
                Role.name.label("role"),
                ProtocolVersion.version.label("protocol_version"),
                Protocol.id.label("protocol_id"),
                Protocol.name.label("protocol"),
                Vendor.id.label("vendor_id"),
                Vendor.trade_name,
                Vendor.statutory_name,
                Vendor.kvk_number,
                ApplicationVersionQualification.qualification_date,
                ApplicationVersionQualification.created_at,
                ApplicationVersionQualification.modified_at,
            )
            .outerjoin(ApplicationVersionQualification.application_version)
            .outerjoin(ApplicationVersionQualification.protocol_version)
            .outerjoin(ApplicationVersion.application)
            .outerjoin(Application.roles)
            .outerjoin(ApplicationRole.role)
            .outerjoin(Application.system_types)
            .outerjoin(ApplicationType.system_type)
            .outerjoin(ProtocolVersion.protocol)
            .outerjoin(Application.vendor)
            .limit(limit)
            .offset(offset)
        )

        results = self.session.execute(
            stmt,
        )

        return results

    def total_qualified_vendors(self) -> int:
        stmt = (
            select(
                func.count(),
            )
            .outerjoin(ApplicationVersionQualification.application_version)
            .outerjoin(ApplicationVersionQualification.protocol_version)
            .outerjoin(ApplicationVersion.application)
            .outerjoin(Application.roles)
            .outerjoin(ApplicationRole.role)
            .outerjoin(Application.system_types)
            .outerjoin(ApplicationType.system_type)
            .outerjoin(ProtocolVersion.protocol)
            .outerjoin(Application.vendor)
        )
        result = self.session.execute(stmt).scalar()
        if result is None:
            return 0

        return result
