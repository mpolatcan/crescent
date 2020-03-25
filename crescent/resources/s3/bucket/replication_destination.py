from crescent.core import Model, Validator
from .access_control_translation import AccessControlTranslation
from .encryption_configuration import EncryptionConfiguration
from .constants import AllowedValues, RequiredProperties


class ReplicationDestination(Model):
    @Validator.validate(type=AccessControlTranslation, required_properties=RequiredProperties.ACCESS_CONTROL_TRANSLATION)
    def AccessControlTranslation(self, value: AccessControlTranslation):
        return self._set_field(self.AccessControlTranslation.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def Account(self, value: str):
        return self._set_field(self.Account.__name__, value)

    @Validator.validate(type=str)
    def Bucket(self, value: str):
        return self._set_field(self.Bucket.__name__, value)

    @Validator.validate(type=EncryptionConfiguration, required_properties=RequiredProperties.ENCRYPTION_CONFIGURATION)
    def EncryptionConfiguration(self, value: EncryptionConfiguration):
        return self._set_field(self.EncryptionConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=str, allowed_values=AllowedValues.REPLICATION_DESTINATION_SC)
    def StorageClass(self, value: str):
        return self._set_field(self.StorageClass.__name__, value)
