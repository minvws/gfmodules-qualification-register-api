import uuid

import inject
import pytest

from app.db.entities.vendor import Vendor
from app.db.repository_factory import RepositoryFactory
from app.db.services.vendor_database_service import VendorDatabaseService
from app.dto.VendorDto import VendorDto


@pytest.fixture()
def vendor_repository(mocker):
    vendor_repository = mocker.Mock()
    mocker.patch.object(
        inject.instance(RepositoryFactory),
        "get_repository",
        return_value=vendor_repository,
    )
    yield vendor_repository


def test_get(injector, mocker, vendor_repository):
    uuid_ = uuid.uuid4()
    system_type = Vendor(id=uuid_, kvk_number="000000001", trade_name="Vendor A - Trade Name",
                         statutory_name="Vendor A - Statutory Name")
    expected = VendorDto(id=uuid_, kvk_number="000000001", trade_name="Vendor A - Trade Name",
                         statutory_name="Vendor A - Statutory Name", applications=[])

    mocker.patch.object(vendor_repository, "get", return_value=system_type)

    service = VendorDatabaseService()
    actual = service.get(uuid_)

    assert actual == expected


def test_get_all(injector, mocker, vendor_repository):
    uuid_ = uuid.uuid4()
    system_types = [Vendor(id=uuid_, kvk_number="000000001", trade_name="Vendor A - Trade Name",
                           statutory_name="Vendor A - Statutory Name"),
                    Vendor(id=uuid_, kvk_number="000000002", trade_name="Vendor B - Trade Name",
                           statutory_name="Vendor B - Statutory Name")]
    expected = [VendorDto(id=uuid_, kvk_number="000000001", trade_name="Vendor A - Trade Name",
                          statutory_name="Vendor A - Statutory Name", applications=[]),
                VendorDto(id=uuid_, kvk_number="000000002", trade_name="Vendor B - Trade Name",
                          statutory_name="Vendor B - Statutory Name", applications=[])]

    mocker.patch.object(vendor_repository, "get_all", return_value=system_types)

    service = VendorDatabaseService()
    actual = service.get_all()

    assert actual == expected


def test_get_with_applications(injector, mocker, vendor_repository):
    pytest.skip("Test get vendor with applications ")
