from typing import Sequence, List

from app.db.entities.system_type import SystemType
from app.schemas.system_type.schema import SystemTypeDto


def map_system_type_entities_to_dtos(entities: Sequence[SystemType]) -> List[SystemTypeDto]:
    return [map_system_type_entity_to_dto(system_type) for system_type in entities]


def map_system_type_entity_to_dto(entity: SystemType) -> SystemTypeDto:
    return SystemTypeDto(
        id=entity.id, name=entity.name, description=entity.description
    )
