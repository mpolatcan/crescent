from crescent.core.constants import get_values


class _RequiredProperties:
    class StreamEncryption:
        ENCRYPTION_TYPE = "EncryptionType"
        KEY_ID = "KeyId"

# -----------------------------------------------------------


class ModelRequiredProperties:
    STREAM_ENCRYPTION = get_values(_RequiredProperties.StreamEncryption)

