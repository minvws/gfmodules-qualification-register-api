from typing import Sequence, List

from app.db.entities.healthcare_provider import HealthcareProvider
from app.schemas.healthcare_provider.schema import HealthcareProviderDto


def map_healthcare_provider_entity_to_dto(entity: HealthcareProvider) -> HealthcareProviderDto:
    return HealthcareProviderDto(
        id=entity.id, ura_code=entity.ura_code, agb_code=entity.agb_code
    )


def map_healthcare_provider_entities_to_dtos(
        entities: Sequence[HealthcareProvider],
) -> List[HealthcareProviderDto]:
    return [map_healthcare_provider_entity_to_dto(entity) for entity in entities]
