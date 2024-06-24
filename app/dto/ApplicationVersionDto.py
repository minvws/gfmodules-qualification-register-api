from uuid import UUID

from pydantic import BaseModel


class ApplicationVersionDto(BaseModel):
    id: UUID
    version: str
