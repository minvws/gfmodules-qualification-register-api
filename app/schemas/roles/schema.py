from uuid import UUID

from gfmodules_python_shared.schema.base_model_schema import BaseModelConfig


class RoleDto(BaseModelConfig):
    id: UUID
    name: str
    description: str | None
