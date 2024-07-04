from uuid import UUID

from pydantic import BaseModel


class RoleDto(BaseModel):
    id: UUID
    name: str
    description: str | None
