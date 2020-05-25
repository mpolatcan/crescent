from crescent.core.constants import get_values


class ConnectionType:
    INTERNET = "INTERNET"
    VPC_LINK = "VPC_LINK"


class ContentHandlingStrategy:
    CONVERT_TO_BINARY = "CONVERT_TO_BINARY"
    CONVERT_TO_TEXT = "CONVERT_TO_TEXT"


class IntegrationType:
    AWS = "AWS"
    AWS_PROXY = "AWS_PROXY"
    HTTP = "HTTP"
    HTTP_PROXY = "HTTP_PROXY"
    MOCK = "MOCK"


class PassthroughBehavior:
    WHEN_NO_MATCH = "WHEN_NO_MATCH"
    NEVER = "NEVER"
    WHEN_NO_TEMPLATES = "WHEN_NO_TEMPLATES"


class AllowedValues:
    CONNECTION_TYPE = get_values(ConnectionType)
    CONTENT_HANDLING_STRATEGY = get_values(ContentHandlingStrategy)
    INTEGRATION_TYPE = get_values(IntegrationType)
    PASSTHROUGH_BEHAVIOR = get_values(PassthroughBehavior)


class _RequiredProperties:
    class Integration:
        API_ID = "ApiId"
        INTEGRATION_TYPE = "IntegrationType"


class ResourceRequiredProperties:
    INTEGRATION = get_values(_RequiredProperties.Integration)