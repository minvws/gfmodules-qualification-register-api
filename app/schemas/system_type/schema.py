from uuid import UUID

from app.schemas.default import BaseModelConfig


class SystemTypeDto(BaseModelConfig):
    id: UUID
    name: str
    description: str | None
