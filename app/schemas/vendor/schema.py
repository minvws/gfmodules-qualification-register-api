from typing import Sequence
from uuid import UUID

from gfmodules_python_shared.schema.base_model_schema import BaseModelConfig

from app.schemas.application_summary.schema import ApplicationSummaryDto


class VendorDto(BaseModelConfig):
    id: UUID
    trade_name: str
    statutory_name: str
    kvk_number: str
    applications: Sequence[ApplicationSummaryDto]


class VendorSummaryDto(BaseModelConfig):
    id: UUID
    trade_name: str
    statutory_name: str
    kvk_number: str
