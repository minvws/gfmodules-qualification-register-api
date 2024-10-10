import pytest
from gfmodules_python_shared.schema.pagination.page_schema import Page

from app.db.services.vendor_service import VendorService


@pytest.mark.parametrize("context", ("role", "system_type", "vendor"))
def test_get(context: str, request: pytest.FixtureRequest):
    service = request.getfixturevalue(f"{context}_service")
    dto = request.getfixturevalue(f"{context}_dto")
    assert service.get(dto.id) == dto


@pytest.mark.parametrize(
    "context", ("role", "system_type", "vendor", "vendor_qualification")
)
def test_get_paginated(context: str, request: pytest.FixtureRequest):
    service = request.getfixturevalue(f"{context}_service")
    dto = request.getfixturevalue(f"{context}_dto")
    assert service.get_paginated(limit=10, offset=0) == Page(
        items=[dto], limit=10, offset=0, total=1
    )


@pytest.mark.parametrize("context", ("vendor", "vendor_with_applications"))
def test_get_paginated_multiple_items(
    context: str, vendor_service: VendorService, request: pytest.FixtureRequest
):
    items = request.getfixturevalue(f"{context}_dtos")
    assert vendor_service.get_paginated(limit=10, offset=0) == Page(
        items=list(items),
        limit=10,
        offset=0,
        total=2,
    )
