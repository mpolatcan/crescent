from crescent.core.constants import get_values


class _RequiredProperties:
    class RouteResponse:
        API_ID = "ApiId"
        ROUTE_ID = "RouteId"
        ROUTE_RESPONSE_KEY = "RouteResponseKey"


class ResourceRequiredProperties:
    ROUTE_RESPONSE = get_values(_RequiredProperties.RouteResponse)
