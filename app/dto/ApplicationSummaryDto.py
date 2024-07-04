from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ApplicationSummaryDto(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    modified_at: datetime
