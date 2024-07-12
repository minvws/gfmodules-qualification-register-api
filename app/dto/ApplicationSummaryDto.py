from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class ApplicationSummaryDto(BaseModel):
    id: UUID
    name: str
    created_at: datetime = Field(serialization_alias="createdAt")
    modified_at: datetime = Field(serialization_alias="modifiedAt")
