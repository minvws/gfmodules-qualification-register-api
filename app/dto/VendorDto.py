from typing import Sequence
from uuid import UUID

from pydantic import BaseModel

from app.dto.ApplicationSummaryDto import ApplicationSummaryDto


class VendorDto(BaseModel):
    id: UUID
    trade_name: str
    statutory_name: str
    kvk_number: str
    applications: Sequence[ApplicationSummaryDto]
