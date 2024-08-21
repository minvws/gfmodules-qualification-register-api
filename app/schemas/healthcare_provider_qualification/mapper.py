from typing import Sequence, List

from app.db.entities.healthcare_provider_qualification import (
    HealthcareProviderQualification,
)
from app.schemas.healthcare_provider_qualification.schema import (
    QualifiedHealthcareProviderDTO,
)


def flatten_healthcare_provider_qualification(
    data: Sequence[HealthcareProviderQualification],
) -> List[QualifiedHealthcareProviderDTO]:
    results: List[QualifiedHealthcareProviderDTO] = []
    for entry in data:
        for (
            qualified_app_version
        ) in entry.protocol_version.qualified_application_versions:
            results.append(
                QualifiedHealthcareProviderDTO(
                    provider_id=entry.healthcare_provider_id,
                    provider_name=entry.healthcare_provider.statutory_name,
                    protocol=entry.protocol_version.protocol.name,
                    protocol_version=entry.protocol_version.version,
                    application_name=qualified_app_version.application_version.application.name,
                    application_version=qualified_app_version.application_version.version,
                    qualification_date=entry.qualification_date,
                )
            )

    return results
