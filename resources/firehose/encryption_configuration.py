from resources.shared import BaseModel
from resources.firehose import KMSEncryptionConfig

class EncryptionConfiguration(BaseModel):
    __PROPERTY_KMS_ENCRYPTION_CONFIG = "KMSEncryptionConfig"
    __PROPERTY_NO_ENCRYPTION_CONFIG = "NoEncryptionConfig"

    def kms_encryption_config(self, value: KMSEncryptionConfig):
        return self._add_field(self.__PROPERTY_KMS_ENCRYPTION_CONFIG, value.create())

    def no_encryption_config(self, value: str):
        return self._add_field(self.__PROPERTY_NO_ENCRYPTION_CONFIG, value)
