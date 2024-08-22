import datetime

from app.db.entities.application import Application
from app.db.entities.application_version import ApplicationVersion
from app.db.entities.application_version_qualification import (
    ApplicationVersionQualification,
)
from app.db.entities.protocol import Protocol
from app.db.entities.protocol_version import ProtocolVersion
from app.db.entities.role import Role
from app.db.entities.system_type import SystemType
from app.db.entities.vendor import Vendor
from app.db.repository.application_repository import ApplicationRepository
from app.db.repository.application_version_qualification_repository import (
    ApplicationVersionQualificationRepository,
)
from app.db.services.vendor_qualification_service import VendorQualificationService
from app.schemas.vendor_qualifications.schema import QualifiedVendorDTO


class TestVendorQualityService:

    def test_get_paginated_should_return_paginated_vendor_qualifications(
        self,
        mock_vendor: Vendor,
        mock_application: Application,
        mock_application_version: ApplicationVersion,
        mock_system_type: SystemType,
        mock_role: Role,
        mock_protocol: Protocol,
        mock_protocol_version: ProtocolVersion,
        vendor_qualification_service: VendorQualificationService,
        application_repository: ApplicationRepository,
        application_version_qualification_repository: ApplicationVersionQualificationRepository,
    ):
        mock_application_qualification = ApplicationVersionQualification(
            application_version=mock_application_version,
            protocol_version=mock_protocol_version,
            qualification_date=datetime.date.today(),
        )

        application_repository.create(mock_application)
        application_version_qualification_repository.create(
            mock_application_qualification
        )

        expected_qualified_vendor = [
            QualifiedVendorDTO(
                vendor_id=mock_vendor.id,
                vendor_name=mock_vendor.trade_name,
                application_name=mock_application.name,
                version=mock_application_version.version,
                system_type=mock_system_type.name,
                role=mock_role.name,
                qualification_date=mock_application_qualification.qualification_date,
                protocol_version=mock_protocol.name,
                protocol_name=mock_protocol.name,
            )
        ]

        page = vendor_qualification_service.get_paginated(limit=10, offset=0)
        actual = page.items

        assert actual == expected_qualified_vendor
