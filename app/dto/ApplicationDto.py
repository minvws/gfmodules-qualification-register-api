from uuid import UUID

from pydantic import BaseModel


class ApplicationDto(BaseModel):
    id: UUID
    name: str

