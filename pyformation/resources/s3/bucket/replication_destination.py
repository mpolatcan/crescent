from pyformation.core import Model, Validator
from .access_control_translation import AccessControlTranslation
from .encryption_configuration import EncryptionConfiguration


class ReplicationDestination(Model):
    @Validator.validate(type=AccessControlTranslation)
    def AccessControlTranslation(self, value: AccessControlTranslation):
        return self._set_field(self.AccessControlTranslation.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def Account(self, value: str):
        return self._set_field(self.Account.__name__, value)

    @Validator.validate(type=str)
    def Bucket(self, value: str):
        return self._set_field(self.Bucket.__name__, value)

    @Validator.validate(type=EncryptionConfiguration)
    def EncryptionConfiguration(self, value: EncryptionConfiguration):
        return self._set_field(self.EncryptionConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def StorageClass(self, value: str):
        return self._set_field(self.StorageClass.__name__, value)
