from typing import Sequence, TYPE_CHECKING

from gfmodules_python_shared.repository.repository_base import RepositoryBase, TArgs
from gfmodules_python_shared.session.db_session import DbSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.db.entities.application import Application
from app.db.entities.application_version import ApplicationVersion
from app.db.entities.application_version_qualification import (
    ApplicationVersionQualification,
)
from app.db.entities.protocol_version import ProtocolVersion


class ApplicationVersionQualificationRepository(
    RepositoryBase[ApplicationVersionQualification]
):
    def __init__(self, db_session: DbSession) -> None:
        super().__init__(session=db_session, cls_model=ApplicationVersionQualification)

    def get_qualified_application_versions(
        self, **kwargs: TArgs
    ) -> Sequence[ApplicationVersionQualification]:
        stmt = (
            select(ApplicationVersionQualification)
            .options(
                selectinload(ApplicationVersionQualification.application_version)
                .selectinload(ApplicationVersion.application)
                .selectinload(Application.vendor)
            )
            .options(
                selectinload(
                    ApplicationVersionQualification.protocol_version
                ).selectinload(ProtocolVersion.protocol)
            )
        ).filter_by(**kwargs)

        results = self.session.scalars_all(stmt)
        # ToDo: remove this temporary solution once return any from gfmodules is resolved
        if TYPE_CHECKING:
            if not isinstance(results, Sequence):
                raise TypeError(f"Unexpected result type: {type(results)}")

        return results
