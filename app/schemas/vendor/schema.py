from typing import Sequence
from uuid import UUID

from app.schemas.application_summary.schema import ApplicationSummaryDto
from app.schemas.default import BaseModelConfig


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
