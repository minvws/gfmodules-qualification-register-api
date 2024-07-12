from datetime import datetime
from typing import Sequence
from uuid import UUID

from pydantic import BaseModel, Field

from app.dto.ApplicationVersionDto import ApplicationVersionDto
from app.dto.RoleDto import RoleDto
from app.dto.SystemTypeDto import SystemTypeDto
from app.dto.VendorSummaryDto import VendorSummaryDto


class ApplicationWithVendorDto(BaseModel):
    id: UUID
    name: str
    created_at: datetime = Field(serialization_alias="createdAt")
    modified_at: datetime = Field(serialization_alias="modifiedAt")
    vendor: VendorSummaryDto
    versions: Sequence[ApplicationVersionDto]
    roles: Sequence[RoleDto]
    system_types: Sequence[SystemTypeDto] = Field(serialization_alias="systemTypes")




