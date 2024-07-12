from uuid import UUID

from pydantic import BaseModel, Field


class VendorSummaryDto(BaseModel):
    id: UUID
    trade_name: str = Field(serialization_alias="tradeName")
    statutory_name: str = Field(serialization_alias="statutoryName")
    kvk_number: str = Field(serialization_alias="kvkNumber")
