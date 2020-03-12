from pyformation import PyformationModel
from .kms_encryption_config import KMSEncryptionConfig


class EncryptionConfiguration(PyformationModel):
    def KMSEncryptionConfig(self, value: KMSEncryptionConfig):
        return self._set_field(self.KMSEncryptionConfig.__name__, value.__to_dict__())

    def NoEncryptionConfig(self, value: str):
        return self._set_field(self.NoEncryptionConfig.__name__, value)
