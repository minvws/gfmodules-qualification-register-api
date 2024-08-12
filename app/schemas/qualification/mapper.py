import datetime
from typing import Sequence, List

from app.db.entities.healthcare_provider import HealthcareProvider
from app.schemas.qualification.schema import QualificationDto


def map_healthcare_provider_entities_to_qualification_dtos(
    entities: Sequence[HealthcareProvider],
) -> Sequence[QualificationDto]:
    return [dto for dtos in entities for dto in map_healthcare_provider_to_qualification_dto(dtos)]


def map_healthcare_provider_to_qualification_dto(entity: HealthcareProvider) -> List[QualificationDto]:
    qualifications = []
    for healthcare_provider_application_version in entity.application_versions:
        for (
            system_type
        ) in (
            healthcare_provider_application_version.application_version.application.system_types
        ):
            for (
                role
            ) in (
                healthcare_provider_application_version.application_version.application.roles
            ):
                for healthcare_provider_qualification in entity.qualified_protocols:
                    qualifications.append(
                        QualificationDto(
                            healthcare_provider_id=entity.id,
                            healthcare_provider_name=entity.trade_name,
                            application_id=healthcare_provider_application_version.application_version.application.id,
                            application_name=healthcare_provider_application_version.application_version.application.name,
                            application_version_id=healthcare_provider_application_version.application_version.id,
                            application_version=healthcare_provider_application_version.application_version.version,
                            system_type_id=system_type.system_type.id,
                            system_type=system_type.system_type.name,
                            role_id=role.role.id,
                            role=role.role.name,
                            qualification_date=datetime.date.today(),
                            protocol_id=healthcare_provider_qualification.protocol_version.protocol.id,
                            protocol_name=healthcare_provider_qualification.protocol_version.protocol.name,
                            protocol_type=healthcare_provider_qualification.protocol_version.protocol.protocol_type,
                            protocol_version_id=healthcare_provider_qualification.protocol_version.id,
                            protocol_version=healthcare_provider_qualification.protocol_version.version,
                        )
                    )
    return qualifications
