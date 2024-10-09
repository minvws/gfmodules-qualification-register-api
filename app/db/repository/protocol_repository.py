from typing import Any

from gfmodules_python_shared.repository.base import RepositoryBase
from sqlalchemy import ColumnExpressionArgument

from app.db.entities.protocol import Protocol


class ProtocolRepository(RepositoryBase[Protocol]):
    @property
    def order_by(self) -> tuple[ColumnExpressionArgument[Any] | str, ...]:
        return (Protocol.created_at.desc(),)
