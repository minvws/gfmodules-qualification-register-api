from datetime import datetime

from uuid import uuid4

from app.db.entities.application import Application
from app.schemas.application_summary.mapper import map_application_entity_to_summary_dto
from app.schemas.application_summary.schema import ApplicationSummaryDto


def test_map_application_entity_to_summary_dto() -> None:
    expected_uuid = uuid4()
    expected_name = "Example application"
    expected_created_at = datetime.now()
    expected_modified_at = datetime.now()

    expected_summary_dto = ApplicationSummaryDto(
        id=expected_uuid,
        name=expected_name,
        created_at=expected_created_at,
        modified_at=expected_modified_at,
    )

    application = Application(
        id=expected_uuid,
        name=expected_name,
        created_at=expected_created_at,
        modified_at=expected_modified_at,
    )

    result = map_application_entity_to_summary_dto(application)
    assert result == expected_summary_dto
