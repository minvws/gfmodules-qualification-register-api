import pytest
from uuid import uuid4

from app.db.entities.protocol import Protocol
from app.db.entities.protocol_version import ProtocolVersion
from app.schemas.enums.protocol_types import ProtocolTypes
from app.schemas.protocol.mapper import map_protocol_type_to_enum, map_protocol_version_entity_to_dto, \
    map_protocol_entity_to_dto
from app.schemas.protocol.schema import ProtocolVersionDto, ProtocolDto


@pytest.mark.parametrize("test_input,expected", [
    ("InformationStandard", ProtocolTypes.INFORMATION_STANDARD),
    ("Directive", ProtocolTypes.DIRECTIVE),
])
def test_map_protocol_type_to_enum(test_input, expected) -> None:
    result = map_protocol_type_to_enum(test_input)

    assert result == expected


@pytest.mark.parametrize("test_input,exception_type,exception_match", [
    ("Non existing", ValueError, "Unknown protocol type: Non existing")
])
def test_map_incorrect_protocol_type_raises_exception(test_input, exception_type, exception_match) -> None:
    with pytest.raises(exception_type, match=exception_match):
        map_protocol_type_to_enum(test_input)


def test_map_protocol_version_entity_to_dto() -> None:
    expected_uuid = uuid4()
    expected_version = "1"
    expected_description = "This is the expected description"
    expected_protocol_version_dto = ProtocolVersionDto(
        id=expected_uuid,
        version=expected_version,
        description=expected_description,
    )

    protocol_version = ProtocolVersion(
        id=expected_uuid,
        version=expected_version,
        description=expected_description,
    )

    result = map_protocol_version_entity_to_dto(protocol_version)
    assert result == expected_protocol_version_dto


def test_map_protocol_entity_to_dto() -> None:
    expected_uuid = uuid4()
    expected_name = "This is the expected name"
    expected_description = "This is the expected description"
    expected_protocol_type = ProtocolTypes.INFORMATION_STANDARD
    expected_versions = []

    expected_protocol_dto = ProtocolDto(
        id=expected_uuid,
        versions=expected_versions,
        protocol_type=expected_protocol_type,
        name=expected_name,
        description=expected_description,
    )

    protocol = Protocol(
        id=expected_uuid,
        protocol_type=expected_protocol_type,
        name=expected_name,
        description=expected_description,
        versions=[]
    )

    result = map_protocol_entity_to_dto(protocol)
    assert result == expected_protocol_dto


def test_map_protocol_entity_with_versions_to_dto() -> None:
    expected_protocol_version_dto = get_example_protocol_version_dto()

    expected_uuid = uuid4()
    expected_name = "This is the expected name"
    expected_description = "This is the expected description"
    expected_protocol_type = ProtocolTypes.INFORMATION_STANDARD
    expected_versions = [
        expected_protocol_version_dto
    ]

    expected_protocol_dto = ProtocolDto(
        id=expected_uuid,
        versions=expected_versions,
        protocol_type=expected_protocol_type,
        name=expected_name,
        description=expected_description,
    )

    protocol = Protocol(
        id=expected_uuid,
        protocol_type=expected_protocol_type,
        name=expected_name,
        description=expected_description,
        versions=[
            ProtocolVersion(
                id=expected_protocol_version_dto.id,
                version=expected_protocol_version_dto.version,
                description=expected_protocol_version_dto.description,
            )
        ]
    )

    result = map_protocol_entity_to_dto(protocol)
    assert result == expected_protocol_dto


def get_example_protocol_version_dto() -> ProtocolVersionDto:
    return ProtocolVersionDto(
        id=uuid4(),
        version="1",
        description="This is the expected ProtocolVersionDto description",
    )