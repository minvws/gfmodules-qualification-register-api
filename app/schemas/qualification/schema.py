from gfmodules_python_shared.schema.base_model_schema import BaseModelConfig
from uuid import UUID
from datetime import date


class QualificationDto(BaseModelConfig):
    healthcare_provider_id: UUID
    healthcare_provider_name: str
    application_id: UUID
    application_name: str
    application_version_id: UUID
    application_version: str
    system_type_id: UUID
    system_type: str
    role_id: UUID
    role: str
    qualification_date: date
    protocol_id: UUID
    protocol_name: str
    protocol_type: str
    protocol_version_id: UUID
    protocol_version: str
