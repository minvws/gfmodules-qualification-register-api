from typing import TypeAlias, Union
from .application_service import ApplicationService
from .healthcare_provider_service import HealthcareProviderService
from .role_service import RoleService
from .system_type_service import SystemTypeService
from .vendor_qualification_service import VendorQualificationService
from .vendor_service import VendorService


Service: TypeAlias = Union[
    ApplicationService,
    HealthcareProviderService,
    RoleService,
    SystemTypeService,
    VendorQualificationService,
    VendorService,
]
