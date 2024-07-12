from typing import Sequence
from uuid import UUID

from pydantic import BaseModel, Field

from app.dto.ApplicationSummaryDto import ApplicationSummaryDto


class VendorDto(BaseModel):
    id: UUID
    trade_name: str = Field(serialization_alias="tradeName")
    statutory_name: str = Field(serialization_alias="statutoryName")
    kvk_number: str = Field(serialization_alias="kvkNumber")
    applications: Sequence[ApplicationSummaryDto]
