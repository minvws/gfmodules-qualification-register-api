from datetime import datetime
from typing import List, Literal, get_args
from uuid import UUID, uuid4

from gfmodules_python_shared.schema.sql_model import SQLModelBase
from sqlalchemy import TIMESTAMP, Enum, String, types
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.entities import protocol_version

ProtocolTypes = Literal["InformationStandard", "Directive"]


class Protocol(SQLModelBase):
    __tablename__ = "protocols"

    id: Mapped[UUID] = mapped_column(
        "id",
        types.Uuid,
        primary_key=True,
        nullable=False,
        default=uuid4,
    )
    protocol_type: Mapped[ProtocolTypes] = mapped_column(
        "protocol_type",
        Enum(
            *get_args(ProtocolTypes),
            name="protocol_type",
            create_constraint=True,
            validate_strings=True,
        ),
    )
    name: Mapped[str] = mapped_column("name", String(150), nullable=False)
    description: Mapped[str] = mapped_column("description", String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        "created_at", TIMESTAMP, nullable=False, default=datetime.now()
    )
    modified_at: Mapped[datetime] = mapped_column(
        "modified_at", TIMESTAMP, nullable=False, default=datetime.now()
    )

    versions: Mapped[List["protocol_version.ProtocolVersion"]] = relationship(
        back_populates="protocol", lazy="selectin", cascade="all, delete, delete-orphan"
    )
