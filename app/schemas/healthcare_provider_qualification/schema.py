from datetime import date
from uuid import UUID

from app.schemas.default import BaseModelConfig


class QualifiedHealthcareProviderDTO(BaseModelConfig):
    provider_id: UUID
    provider_name: str
    protocol: str
    protocol_version: str
    application_name: str
    application_version: str
    qualification_date: date
