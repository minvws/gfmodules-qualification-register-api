from uuid import UUID

from pydantic import BaseModel

from app.dto.ApplicationDto import ApplicationDto


class ApplicationVersionDto(BaseModel):
    id: UUID
    application: ApplicationDto
    version: str
