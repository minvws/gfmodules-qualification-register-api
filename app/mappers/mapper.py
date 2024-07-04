import datetime
from typing import Sequence

from app.db.entities.application import Application
from app.db.entities.application_version import ApplicationVersion
from app.db.entities.healthcare_provider import HealthcareProvider
from app.db.entities.role import Role
from app.db.entities.system_type import SystemType
from app.dto.ApplicationSummaryDto import ApplicationSummaryDto
from app.dto.ApplicationWithVendorDto import ApplicationWithVendorDto

from app.db.entities.vendor import Vendor
from app.dto.ApplicationVersionDto import ApplicationVersionDto
from app.dto.HealthcareProviderDto import HealthcareProviderDto
from app.dto.RoleDto import RoleDto
from app.dto.SystemTypeDto import SystemTypeDto
from app.dto.VendorDto import VendorDto
from app.dto.VendorSummaryDto import VendorSummaryDto
from app.dto.qualification_dto import QualificationDto


class Mapper:
    @staticmethod
    def to_healthcare_provider_dto(entity: HealthcareProvider) -> HealthcareProviderDto:
        return HealthcareProviderDto(
            id=entity.id, ura_code=entity.ura_code, agb_code=entity.agb_code
        )

    @staticmethod
    def to_healthcare_provider_dtos(
        entities: Sequence[HealthcareProvider],
    ) -> Sequence[HealthcareProviderDto]:
        return [Mapper.to_healthcare_provider_dto(entity) for entity in entities]

    @staticmethod
    def to_qualification_dtos(
        entities: Sequence[HealthcareProvider],
    ) -> Sequence[QualificationDto]:
        return [dto for dtos in entities for dto in Mapper.to_qualification_dto(dtos)]

    @staticmethod
    def to_application_dtos(
        entities: Sequence[Application],
    ) -> Sequence[ApplicationWithVendorDto]:
        return [Mapper.to_application_dto(entity) for entity in entities]

    @staticmethod
    def to_role_dtos(entities: Sequence[Role]) -> Sequence[RoleDto]:
        return [Mapper.to_role_dto(role) for role in entities]

    @staticmethod
    def to_system_type_dtos(entities: Sequence[SystemType]) -> Sequence[SystemTypeDto]:
        return [Mapper.to_system_type_dto(system_type) for system_type in entities]

    @staticmethod
    def to_vendor_dtos(entities: Sequence[Vendor]) -> Sequence[VendorDto]:
        return [Mapper.to_vendor_dto(vendor) for vendor in entities]

    @staticmethod
    def to_qualification_dto(entity: HealthcareProvider) -> Sequence[QualificationDto]:
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

    @staticmethod
    def to_application_dto(entity: Application) -> ApplicationWithVendorDto:
        return ApplicationWithVendorDto(
            id=entity.id,
            name=entity.name,
            created_at=entity.created_at,
            modified_at=entity.modified_at,
            vendor=Mapper.to_vendor_summary_dto(entity.vendor),
            versions=[
                Mapper.to_application_version_dto(version)
                for version in entity.versions
            ],
            roles=[Mapper.to_role_dto(role.role) for role in entity.roles],
            system_types=[
                Mapper.to_system_type_dto(system_type.system_type)
                for system_type in entity.system_types
            ],
        )

    @staticmethod
    def to_application_summary_dto(entity: Application) -> ApplicationSummaryDto:
        return ApplicationSummaryDto(
            id=entity.id,
            name=entity.name,
            created_at=entity.created_at,
            modified_at=entity.modified_at,
        )

    @staticmethod
    def to_vendor_summary_dto(entity: Vendor) -> VendorSummaryDto:
        return VendorSummaryDto(
            id=entity.id,
            trade_name=entity.trade_name,
            statutory_name=entity.statutory_name,
            kvk_number=entity.kvk_number,
        )

    @staticmethod
    def to_application_version_dto(entity: ApplicationVersion) -> ApplicationVersionDto:
        return ApplicationVersionDto(
            id=entity.id,
            version=entity.version,
        )

    @staticmethod
    def to_role_dto(entity: Role) -> RoleDto:
        return RoleDto(id=entity.id, name=entity.name, description=entity.description)

    @staticmethod
    def to_system_type_dto(entity: SystemType) -> SystemTypeDto:
        return SystemTypeDto(
            id=entity.id,
            name=entity.name,
            description=entity.description,
        )

    @staticmethod
    def to_vendor_dto(entity: Vendor) -> VendorDto:
        return VendorDto(
            id=entity.id,
            trade_name=entity.trade_name,
            statutory_name=entity.statutory_name,
            kvk_number=entity.kvk_number,
            applications=[
                Mapper.to_application_summary_dto(application)
                for application in entity.applications
            ],
        )
