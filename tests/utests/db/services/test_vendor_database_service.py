import uuid

from datetime import datetime

from app.db.entities.application import Application
from app.db.entities.vendor import Vendor
from app.schemas.application_summary.schema import ApplicationSummaryDto
from app.schemas.vendor.schema import VendorDto


class TestVendorDatabaseService:
    def test_get(self, vendor_repository, vendor_service):
        uuid_ = uuid.uuid4()
        vendor = Vendor(id=uuid_, kvk_number="000000001", trade_name="Vendor A - Trade Name",
                        statutory_name="Vendor A - Statutory Name")
        expected = VendorDto(id=uuid_, kvk_number="000000001", trade_name="Vendor A - Trade Name",
                             statutory_name="Vendor A - Statutory Name", applications=[])

        vendor_repository.create(vendor)

        actual = vendor_service.get(uuid_)

        assert actual == expected

    def test_get_all(self, vendor_repository, vendor_service):
        uuid_a = uuid.uuid4()
        uuid_b = uuid.uuid4()

        vendor_a = Vendor(id=uuid_a, kvk_number="000000001", trade_name="Vendor A - Trade Name",
                          statutory_name="Vendor A - Statutory Name")
        vendor_b = Vendor(id=uuid_b, kvk_number="000000002", trade_name="Vendor B - Trade Name",
                          statutory_name="Vendor B - Statutory Name")
        expected = [VendorDto(id=uuid_a, kvk_number="000000001", trade_name="Vendor A - Trade Name",
                              statutory_name="Vendor A - Statutory Name", applications=[]),
                    VendorDto(id=uuid_b, kvk_number="000000002", trade_name="Vendor B - Trade Name",
                              statutory_name="Vendor B - Statutory Name", applications=[])]

        vendor_repository.create(vendor_a)
        vendor_repository.create(vendor_b)

        actual = vendor_service.get_all()

        assert actual == expected

    def test_get_with_applications(self, vendor_repository, vendor_service):
        uuid_a = uuid.uuid4()
        uuid_b = uuid.uuid4()

        application_a_vendor_a_uuid = uuid.uuid4()
        application_b_vendor_a_uuid = uuid.uuid4()
        application_a_vendor_b_uuid = uuid.uuid4()
        application_b_vendor_b_uuid = uuid.uuid4()

        _datetime = datetime.now()

        applications_a = [
            Application(id=application_a_vendor_a_uuid, name="Application A - Vendor A", created_at=_datetime,
                        modified_at=_datetime),
            Application(id=application_b_vendor_a_uuid, name="Application B - Vendor A", created_at=_datetime,
                        modified_at=_datetime)]
        applications_b = [
            Application(id=application_a_vendor_b_uuid, name="Application A - Vendor B", created_at=_datetime,
                        modified_at=_datetime),
            Application(id=application_b_vendor_b_uuid, name="Application B - Vendor B", created_at=_datetime,
                        modified_at=_datetime)]

        expected_applications_a = [
            ApplicationSummaryDto(id=application_a_vendor_a_uuid, name="Application A - Vendor A", created_at=_datetime,
                                  modified_at=_datetime),
            ApplicationSummaryDto(id=application_b_vendor_a_uuid, name="Application B - Vendor A", created_at=_datetime,
                                  modified_at=_datetime)]
        expected_applications_b = [
            ApplicationSummaryDto(id=application_a_vendor_b_uuid, name="Application A - Vendor B", created_at=_datetime,
                                  modified_at=_datetime),
            ApplicationSummaryDto(id=application_b_vendor_b_uuid, name="Application B - Vendor B", created_at=_datetime,
                                  modified_at=_datetime)]

        vendors_a = Vendor(id=uuid_a, kvk_number="000000001", trade_name="Vendor A - Trade Name",
                          statutory_name="Vendor A - Statutory Name", applications=applications_a)
        vendor_b = Vendor(id=uuid_b, kvk_number="000000002", trade_name="Vendor B - Trade Name",
                          statutory_name="Vendor B - Statutory Name", applications=applications_b)
        expected = [VendorDto(id=uuid_a, kvk_number="000000001", trade_name="Vendor A - Trade Name",
                              statutory_name="Vendor A - Statutory Name", applications=expected_applications_a),
                    VendorDto(id=uuid_b, kvk_number="000000002", trade_name="Vendor B - Trade Name",
                              statutory_name="Vendor B - Statutory Name", applications=expected_applications_b)]

        vendor_repository.create(vendors_a)
        vendor_repository.create(vendor_b)

        actual = vendor_service.get_all()

        assert actual == expected
