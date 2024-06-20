from typing import Sequence

from app.db.entities.HealthcareProvider import HealthcareProvider
from app.dto.HealthcareProviderDto import HealthcareProviderDto


class Mapper:
    @staticmethod
    def to_healthcare_provider_dto(entity: HealthcareProvider) -> HealthcareProviderDto:
        return HealthcareProviderDto(
            id = entity.id,
            ura_code = entity.ura_code,
            agb_code = entity.agb_code
        )


def to_healthcare_provider_dtos(entities: Sequence[HealthcareProvider]) -> Sequence[HealthcareProviderDto]:
    return [Mapper.to_healthcare_provider_dto(entity) for entity in entities]
