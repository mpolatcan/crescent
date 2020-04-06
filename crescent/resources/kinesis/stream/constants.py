from crescent.core.constants import get_values


class _RequiredProperties:
    class StreamEncryption:
        ENCRYPTION_TYPE = "EncryptionType"
        KEY_ID = "KeyId"

    class Stream:
        SHARD_COUNT = "ShardCount"

# -----------------------------------------------------------


class ModelRequiredProperties:
    STREAM_ENCRYPTION = get_values(_RequiredProperties.StreamEncryption)

# -----------------------------------------------------------


class ResourceRequiredProperties:
    STREAM = get_values(_RequiredProperties.Stream)

