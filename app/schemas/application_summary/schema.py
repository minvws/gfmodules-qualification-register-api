from datetime import datetime
from uuid import UUID

from app.schemas.default import BaseModelConfig


class ApplicationSummaryDto(BaseModelConfig):
    id: UUID
    name: str
    created_at: datetime
    modified_at: datetime
