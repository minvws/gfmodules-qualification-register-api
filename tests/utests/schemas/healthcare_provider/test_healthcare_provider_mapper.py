from uuid import uuid4

from app.db.entities.healthcare_provider import HealthcareProvider
from app.schemas.healthcare_provider.mapper import map_healthcare_provider_entity_to_dto, \
    map_healthcare_provider_entities_to_dtos
from app.schemas.healthcare_provider.schema import HealthcareProviderDto


def test_map_healthcare_provider_entity_to_dto() -> None:
    expected_uuid = uuid4()
    expected_ura_code = "URA_CODE"
    expected_agb_code = "AGB_CODE"

    expected_dto = HealthcareProviderDto(
        id=expected_uuid,
        ura_code=expected_ura_code,
        agb_code=expected_agb_code,
    )

    healthcare_provider = HealthcareProvider(
        id=expected_uuid,
        ura_code=expected_ura_code,
        agb_code=expected_agb_code,
    )

    result = map_healthcare_provider_entity_to_dto(healthcare_provider)
    assert result == expected_dto


def test_map_multiple_healthcare_provider_entity_to_dto() -> None:
    expected_uuid = uuid4()
    expected_ura_code = "URA_CODE"
    expected_agb_code = "AGB_CODE"

    expected_dto = HealthcareProviderDto(
        id=expected_uuid,
        ura_code=expected_ura_code,
        agb_code=expected_agb_code,
    )

    healthcare_provider = HealthcareProvider(
        id=expected_uuid,
        ura_code=expected_ura_code,
        agb_code=expected_agb_code,
    )

    result = map_healthcare_provider_entities_to_dtos([healthcare_provider])
    assert result[0] == expected_dto
