from crescent.core import Model
from crescent.functions import AnyFn
from .kms_encryption_config import KMSEncryptionConfig
from typing import Union


class EncryptionConfiguration(Model):
    def KMSEncryptionConfig(self, kms_encryption_conf: KMSEncryptionConfig):
        return self._set_field(self.KMSEncryptionConfig.__name__, kms_encryption_conf)

    def NoEncryptionConfig(self, no_encryption_conf: Union[str, AnyFn]):
        return self._set_field(self.NoEncryptionConfig.__name__, no_encryption_conf)
