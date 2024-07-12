from uuid import UUID
from datetime import date

from pydantic import BaseModel, Field


class QualificationDto(BaseModel):
    healthcare_provider_id: UUID = Field(serialization_alias="healthcarePoviderId")
    healthcare_provider_name: str = Field(serialization_alias="healthcarePoviderName")
    application_id: UUID = Field(serialization_alias="applicationId")
    application_name: str = Field(serialization_alias="applicationName")
    application_version_id: UUID = Field(serialization_alias="applicationVersionId")
    application_version: str = Field(serialization_alias="applicationVersion")
    system_type_id: UUID = Field(serialization_alias="systemTypeId")
    system_type: str = Field(serialization_alias="systemType")
    role_id: UUID = Field(serialization_alias="roleId")
    role: str
    qualification_date: date = Field(serialization_alias="qualificationDate")
    protocol_id: UUID = Field(serialization_alias="protocolId")
    protocol_name: str = Field(serialization_alias="protocolName")
    protocol_type: str = Field(serialization_alias="protocolType")
    protocol_version_id: UUID = Field(serialization_alias="protocolVersionId")
    protocol_version: str = Field(serialization_alias="protocolVersion")
