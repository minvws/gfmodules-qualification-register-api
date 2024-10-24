from datetime import datetime
from uuid import UUID

from gfmodules_python_shared.schema.base_model_schema import BaseModelConfig


class ApplicationSummaryDto(BaseModelConfig):
    id: UUID
    name: str
    created_at: datetime
    modified_at: datetime
