from crescent.core.constants import get_values


class AuthorizationType:
    NONE = "NONE"
    AWS_IAM = "AWS_IAM"
    CUSTOM = "NONE"
    JWT = "JWT"


class _RequiredProperties:
    class Route:
        API_ID = "ApiId"
        ROUTE_KEY = "RouteKey"


class AllowedValues:
    AUTHORIZATION_TYPE = get_values(AuthorizationType)


class ResourceRequiredProperties:
    ROUTE = get_values(_RequiredProperties.Route)
