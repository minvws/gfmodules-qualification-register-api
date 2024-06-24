from uuid import UUID

from pydantic import BaseModel



class VendorSummaryDto(BaseModel):
    id: UUID
    trade_name: str
    statutory_name: str
    kvk_number: str
