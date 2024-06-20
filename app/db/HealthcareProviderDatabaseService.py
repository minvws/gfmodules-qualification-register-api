from typing import List
from uuid import uuid4

from app.dto.HealthcareProviderDto import HealthcareProviderDto


class HealthcareProviderDatabaseService:
    def get_all(self) -> List[HealthcareProviderDto]:
        return [HealthcareProviderDto(
            id=uuid4(),
            ura_code="ura_code",
            agb_code="agb_code"
        )]
