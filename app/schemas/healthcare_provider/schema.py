from typing import List
from uuid import UUID

from gfmodules_python_shared.schema.base_model_schema import BaseModelConfig

from app.schemas.application.schema import ApplicationVersionDto


class HealthcareProviderDto(BaseModelConfig):
    id: UUID
    ura_code: str
    agb_code: str
    application_versions: List[ApplicationVersionDto] = []
