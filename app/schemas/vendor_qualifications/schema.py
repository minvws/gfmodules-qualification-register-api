from uuid import UUID
from datetime import date

from gfmodules_python_shared.schema.base_model_schema import BaseModelConfig


class QualifiedVendorDTO(BaseModelConfig):
    qualification_id: UUID
    application_version_id: UUID
    application_id: UUID
    vendor_id: UUID
    protocol_id: UUID
    system_type_id: UUID
    role_id: UUID
    application_version: str
    application: str
    protocol: str
    protocol_version: str
    system_type: str
    role: str
    kvk_number: str
    trade_name: str
    statutory_name: str
    qualification_date: date
