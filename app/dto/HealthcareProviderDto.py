from typing import List
from uuid import UUID

from pydantic import BaseModel

from app.dto.ApplicationVersionDto import ApplicationVersionDto


class HealthcareProviderDto(BaseModel):
    id: UUID
    ura_code: str
    agb_code: str
    application_versions: List[ApplicationVersionDto] = []
