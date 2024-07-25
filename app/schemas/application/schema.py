from datetime import datetime
from typing import List
from uuid import UUID

from app.schemas.default import BaseModelConfig
from app.schemas.roles.schema import RoleDto
from app.schemas.system_type.schema import SystemTypeDto
from app.schemas.vendor.schema import VendorSummaryDto


class ApplicationVersionDto(BaseModelConfig):
    id: UUID
    version: str


class ApplicationWithVendorDto(BaseModelConfig):
    id: UUID
    name: str
    created_at: datetime
    modified_at: datetime
    vendor: VendorSummaryDto
    versions: List[ApplicationVersionDto] = []
    roles: List[RoleDto] = []
    system_types: List[SystemTypeDto] = []
