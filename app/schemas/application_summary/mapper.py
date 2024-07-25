from app.db.entities.application import Application
from app.schemas.application_summary.schema import ApplicationSummaryDto


def map_application_entity_to_summary_dto(entity: Application) -> ApplicationSummaryDto:
    return ApplicationSummaryDto(
        id=entity.id,
        name=entity.name,
        created_at=entity.created_at,
        modified_at=entity.modified_at,
    )
