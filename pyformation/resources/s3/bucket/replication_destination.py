from pyformation import PyformationModel
from .access_control_translation import AccessControlTranslation
from .encryption_configuration import EncryptionConfiguration


class ReplicationDestination(PyformationModel):
    def AccessControlTranslation(self, value: AccessControlTranslation):
        return self._set_field(self.AccessControlTranslation.__name__, value.__to_dict__())

    def Account(self, value: str):
        return self._set_field(self.Account.__name__, value)

    def Bucket(self, value: str):
        return self._set_field(self.Bucket.__name__, value)

    def EncryptionConfiguration(self, value: EncryptionConfiguration):
        return self._set_field(self.EncryptionConfiguration.__name__, value.__to_dict__())

    def StorageClass(self, value: str):
        return self._set_field(self.StorageClass.__name__, value)
