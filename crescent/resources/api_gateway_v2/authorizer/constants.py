from crescent.core.constants import get_values


class AuthorizerType:
    JWT = "JWT"
    REQUEST = "REQUEST"


class _RequiredProperties:
    class Authorizer:
        API_ID = "ApiId"
        AUTHORIZER_TYPE = "AuthorizerType"
        IDENTITY_SOURCE = "IdentitySource"
        NAME = "Name"


class AllowedValues:
    AUTHORIZER_TYPE = get_values(AuthorizerType)


class ResourceRequiredProperties:
    AUTHORIZER = get_values(_RequiredProperties.Authorizer)
