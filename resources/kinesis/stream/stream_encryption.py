from resources.shared import BaseModel


class StreamEncryption(BaseModel):
    __PROPERTY_ENCRYPTION_TYPE = "EncryptionType"
    __PROPERTY_KEY_ID = "KeyId"

    def encryption_type(self, value: str):
        return self._add_field(self.__PROPERTY_ENCRYPTION_TYPE, value)

    def key_id(self, value: str):
        return self._add_field(self.__PROPERTY_KEY_ID, value)
