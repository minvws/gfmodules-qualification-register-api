from typing import List, Sequence

from app.db.entities.application_version_qualification import (
    ApplicationVersionQualification,
)
from app.schemas.vendor_qualifications.schema import QualifiedVendorDTO


def flatten_vendor_qualifications(
    data: Sequence[ApplicationVersionQualification],
) -> List[QualifiedVendorDTO]:
    results: List[QualifiedVendorDTO] = []
    for entry in data:
        for system_type in entry.application_version.application.system_types:
            for role in entry.application_version.application.roles:
                results.append(
                    QualifiedVendorDTO(
                        vendor_id=entry.application_version.application.vendor_id,
                        vendor_name=entry.application_version.application.vendor.statutory_name,
                        application_name=entry.application_version.application.name,
                        version=entry.application_version.version,
                        system_type=system_type.system_type.name,
                        role=role.role.name,
                        protocol_name=entry.protocol_version.protocol.name,
                        protocol_version=entry.protocol_version.version,
                        qualification_date=entry.qualification_date,
                    )
                )

    return results
