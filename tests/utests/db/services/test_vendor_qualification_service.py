import datetime

from app.db.entities.application import Application
from app.db.entities.application_role import ApplicationRole
from app.db.entities.application_type import ApplicationType
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

    def test_get_all_should_return_all_vendor_qualifications(
        self,
        vendor_qualification_service: VendorQualificationService,
        application_repository: ApplicationRepository,
        application_version_qualification_repository: ApplicationVersionQualificationRepository,
    ):
        mock_vendor = Vendor(
            kvk_number="example",
            trade_name="example",
            statutory_name="example",
        )
        mock_application_version = ApplicationVersion(version="example")
        mock_system_type = SystemType(name="example")
        mock_role = Role(name="example")
        mock_application = Application(
            name="example",
            vendor=mock_vendor,
            versions=[mock_application_version],
            system_types=[],
            roles=[],
        )
        mock_application_role = ApplicationRole(
            application=mock_application, role=mock_role
        )
        mock_application_type = ApplicationType(
            application=mock_application, system_type=mock_system_type
        )
        mock_application.system_types.append(mock_application_type)
        mock_application.roles.append(mock_application_role)
        application_repository.create(mock_application)

        mock_protocol_version = ProtocolVersion(version="example")
        mock_protocol = Protocol(
            protocol_type="InformationStandard",
            name="example",
            versions=[mock_protocol_version],
        )
        mock_application_qualification = ApplicationVersionQualification(
            application_version=mock_application_version,
            protocol_version=mock_protocol_version,
            qualification_date=datetime.date.today(),
        )
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
        actual_qualified_vendor = vendor_qualification_service.get_all()

        assert expected_qualified_vendor == actual_qualified_vendor
