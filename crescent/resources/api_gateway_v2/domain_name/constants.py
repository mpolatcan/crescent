from crescent.core.constants import get_values


class _RequiredPropeties:
    class DomainName:
        DOMAIN_NAME = "DomainName"


class ResourceRequiredProperties:
    DOMAIN_NAME = get_values(_RequiredPropeties.DomainName)