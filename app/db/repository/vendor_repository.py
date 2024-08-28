from typing import Any

from gfmodules_python_shared.repository.repository_base import RepositoryBase
from gfmodules_python_shared.session.db_session import DbSession
from sqlalchemy import Result, select, func

from app.db.entities.application import Application
from app.db.entities.application_role import ApplicationRole
from app.db.entities.application_type import ApplicationType
from app.db.entities.application_version import ApplicationVersion
from app.db.entities.application_version_qualification import (
    ApplicationVersionQualification,
)
from app.db.entities.protocol import Protocol
from app.db.entities.protocol_version import ProtocolVersion
from app.db.entities.role import Role
from app.db.entities.system_type import SystemType
from app.db.entities.vendor import Vendor


class VendorRepository(RepositoryBase[Vendor]):
    def __init__(self, db_session: DbSession):
        super().__init__(session=db_session, cls_model=Vendor)

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

        results = self.session.session.execute(
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
        result = self.session.session.execute(stmt).scalar()
        if result is None:
            return 0

        return result
