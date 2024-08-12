from typing import List
from uuid import UUID

from app.schemas.application.schema import ApplicationVersionDto
from app.schemas.default import BaseModelConfig


class HealthcareProviderDto(BaseModelConfig):
    id: UUID
    ura_code: str
    agb_code: str
    application_versions: List[ApplicationVersionDto] = []
