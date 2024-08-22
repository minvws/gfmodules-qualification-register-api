from uuid import UUID
from datetime import date

from gfmodules_python_shared.schema.base_model_schema import BaseModelConfig


class QualifiedVendorDTO(BaseModelConfig):
    vendor_id: UUID
    vendor_name: str
    application_name: str
    version: str
    system_type: str
    role: str
    qualification_date: date
    protocol_name: str
    protocol_version: str
