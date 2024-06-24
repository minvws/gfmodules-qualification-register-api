from uuid import UUID

from pydantic import BaseModel


class SystemTypeDto(BaseModel):
    id: UUID
    name: str
    description: str | None
