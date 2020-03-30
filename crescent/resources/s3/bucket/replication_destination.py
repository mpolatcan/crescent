from crescent.core import Model, Validator
from .access_control_translation import AccessControlTranslation
from .encryption_configuration import EncryptionConfiguration
from .constants import AllowedValues, ModelRequiredProperties


class ReplicationDestination(Model):
    @Validator.validate(type=AccessControlTranslation, required_properties=ModelRequiredProperties.ACCESS_CONTROL_TRANSLATION)
    def AccessControlTranslation(self, access_control_translation: AccessControlTranslation):
        return self._set_field(self.AccessControlTranslation.__name__, access_control_translation.__to_dict__())

    @Validator.validate(type=str)
    def Account(self, account: str):
        return self._set_field(self.Account.__name__, account)

    @Validator.validate(type=str)
    def Bucket(self, bucket: str):
        return self._set_field(self.Bucket.__name__, bucket)

    @Validator.validate(type=EncryptionConfiguration, required_properties=ModelRequiredProperties.ENCRYPTION_CONFIGURATION)
    def EncryptionConfiguration(self, encryption_conf: EncryptionConfiguration):
        return self._set_field(self.EncryptionConfiguration.__name__, encryption_conf.__to_dict__())

    @Validator.validate(type=str, allowed_values=AllowedValues.REPLICATION_DESTINATION_SC)
    def StorageClass(self, storage_class: str):
        return self._set_field(self.StorageClass.__name__, storage_class)
