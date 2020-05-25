from crescent.core.constants import get_values


class _RequiredProperties:
    class ApiMapping:
        API_ID = "ApiId"
        DOMAIN_NAME = "DomainName"
        STAGE = "Stage"


class ResourceRequiredProperties:
    API_MAPPING = get_values(_RequiredProperties.ApiMapping)