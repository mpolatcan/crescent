class Property:
    STREAM_ENCRYPTION_ENCRYPTION_TYPE = "EncryptionType"
    STREAM_ENCRYPTION_KEY_ID = "KeyId"

# -----------------------------------------------------------


class RequiredProperties:
    STREAM_ENCRYPTION = [
        Property.STREAM_ENCRYPTION_ENCRYPTION_TYPE,
        Property.STREAM_ENCRYPTION_KEY_ID
    ]
