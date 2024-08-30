from datetime import date
from uuid import UUID

from gfmodules_python_shared.schema.base_model_schema import BaseModelConfig


class QualifiedHealthcareProviderDTO(BaseModelConfig):
    qualification_id: UUID
    healthcare_provider_id: UUID
    protocol_id: UUID
    protocol_version_id: UUID
    healthcare_provider: str
    protocol: str
    protocol_type: str
    protocol_version: str
    qualification_date: date
