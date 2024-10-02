from typing import Any

from gfmodules_python_shared.repository.base import RepositoryBase
from sqlalchemy import ColumnExpressionArgument

from app.db.entities import ApplicationVersionQualification


class ApplicationVersionQualificationRepository(
    RepositoryBase[ApplicationVersionQualification]
):
    @property
    def order_by(self) -> tuple[ColumnExpressionArgument[Any] | str, ...]:
        return (ApplicationVersionQualification.created_at.desc(),)
