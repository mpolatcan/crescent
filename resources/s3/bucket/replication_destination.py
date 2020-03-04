from resources.shared.base_model import BaseModel
from resources.s3.bucket.access_control_translation import AccessControlTranslation
from resources.s3.bucket.encryption_configuration import EncryptionConfiguration


class ReplicationDestination(BaseModel):
    __PROPERTY_ACCESS_CONTROL_TRANSLATION = "AccessControlTranslation"
    __PROPERTY_ACCOUNT = "Account"
    __PROPERTY_BUCKET = "Bucket"
    __PROPERTY_ENCRYPTION_CONFIGURATION = "EncryptionConfiguration"
    __PROPERTY_STORAGE_CLASS = "StorageClass"

    def access_control_translation(self, value: AccessControlTranslation):
        return self._add_field(self.__PROPERTY_ACCESS_CONTROL_TRANSLATION, value.create())

    def account(self, value: str):
        return self._add_field(self.__PROPERTY_ACCOUNT, value)

    def bucket(self, value: str):
        return self._add_field(self.__PROPERTY_BUCKET, value)

    def encryption_configuration(self, value: EncryptionConfiguration):
        return self._add_field(self.__PROPERTY_ENCRYPTION_CONFIGURATION, value)

    def storage_class(self, value: str):
        return self._add_field(self.__PROPERTY_STORAGE_CLASS, value)
