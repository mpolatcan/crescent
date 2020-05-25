from crescent.core.constants import get_values


class _RequiredProperties:
    class IntegrationResponse:
        API_ID = "ApiId"
        INTEGRATION_RESPONSE_KEY = "IntegrationResponseKey"


class ResourceRequiredProperties:
    INTEGRATION_RESPONSE = get_values(_RequiredProperties.IntegrationResponse)
