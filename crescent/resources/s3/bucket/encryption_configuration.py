from crescent.core import Model
from crescent.functions import AnyFn
from .constants import ModelRequiredProperties
from typing import Union


class EncryptionConfiguration(Model):
    def __init__(self):
        super(EncryptionConfiguration, self).__init__(required_properties=ModelRequiredProperties.ENCRYPTION_CONFIGURATION)

    def ReplicaKmsKeyID(self, replica_kms_key_id: Union[str, AnyFn]):
        return self._set_field(self.ReplicaKmsKeyID.__name__, replica_kms_key_id)
