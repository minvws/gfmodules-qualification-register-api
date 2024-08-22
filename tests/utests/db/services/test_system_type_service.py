from uuid import uuid4

from app.db.entities.system_type import SystemType
from app.schemas.system_type.schema import SystemTypeDto


class TestSystemTypeService:
    def test_get(self, system_type_repository, system_type_service):
        uuid_ = uuid4()
        system_type = SystemType(id=uuid_, name="System Type A", description=None)
        expected = SystemTypeDto(id=uuid_, name="System Type A", description=None)
        system_type_repository.create(system_type)

        actual = system_type_service.get(uuid_)

        assert actual == expected

    def test_get_paginated(self, system_type_repository, system_type_service):
        uuid_ = uuid4()
        system_type = SystemType(id=uuid_, name="System Type A", description=None)
        expected = [SystemTypeDto(id=uuid_, name="System Type A", description=None)]
        system_type_repository.create(system_type)

        page = system_type_service.get_paginated(limit=10, offset=0)
        actual = page.items

        assert actual == expected
