from crescent.core.constants import get_values


class BillingMode:
    PROVISIONED = "PROVISIONED"
    PAY_PER_REQUEST = "PAY_PER_REQUEST"


class AttributeType:
    S = "S"
    N = "N"
    B = "B"


class KeyType:
    HASH = "HASH"
    RANGE = "RANGE"


class ProjectionType:
    KEYS_ONLY = "KEYS_ONLY"
    INCLUDE = "INCLUDE"
    ALL = "ALL"


class SSEType:
    KMS = "KMS"


class StreamViewType:
    KEYS_ONLY = "KEYS_ONLY"
    NEW_IMAGE = "NEW_IMAGE"
    OLD_IMAGE = "OLD_IMAGE"
    NEW_AND_OLD_IMAGES = "NEW_AND_OLD_IMAGES"


class _RequiredProperties:
    class Table:
        KEY_SCHEMA = "KeySchema"

    class GlobalSecondaryIndex:
        INDEX_NAME = "IndexName"
        KEY_SCHEMA = "KeySchema"
        PROJECTION = "Projection"

    class KeySchema:
        ATTRIBUTE_NAME = "AttributeName"
        KEY_TYPE = "KeyType"

    class LocalSecondaryIndex:
        INDEX_NAME = "IndexName"
        KEY_SCHEMA = "KeySchema"
        PROJECTION = "Projection"

    class ProvisionedThroughput:
        READ_CAPACITY_UNITS = "ReadCapacityUnits"
        WRITE_CAPACITY_UNITS = "WriteCapacityUnits"

    class SSESpecification:
        SSE_ENABLED = "SSEEnabled"

    class StreamSpecification:
        STREAM_VIEW_TYPE = "StreamViewType"

    class TimeToLiveSpecification:
        ATTRIBUTE_NAME = "AttributeName"
        ENABLED = "Enabled"


class AllowedValues:
    BILLING_MODE = get_values(BillingMode)
    ATTRIBUTE_TYPE = get_values(AttributeType)
    KEY_TYPE = get_values(KeyType)
    PROJECTION_TYPE = get_values(ProjectionType)
    SSE_TYPE = get_values(SSEType)
    STREAM_VIEW_TYPE = get_values(StreamViewType)


class ModelRequiredProperties:
    GLOBAL_SECONDARY_INDEX = get_values(_RequiredProperties.GlobalSecondaryIndex)
    KEY_SCHEMA = get_values(_RequiredProperties.KeySchema)
    LOCAL_SECONDARY_INDEX = get_values(_RequiredProperties.LocalSecondaryIndex)
    PROVISIONED_THROUGHPUT = get_values(_RequiredProperties.ProvisionedThroughput)
    SSE_SPECIFICATION = get_values(_RequiredProperties.SSESpecification)
    STREAM_SPECIFICATION = get_values(_RequiredProperties.StreamSpecification)
    TIME_TO_LIVE_SPECIFICATION = get_values(_RequiredProperties.TimeToLiveSpecification)
    TABLE = get_values(_RequiredProperties.Table)
