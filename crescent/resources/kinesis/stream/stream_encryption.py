from crescent.core import Model
from crescent.functions import AnyFn
from .constants import ModelRequiredProperties
from typing import Union


class StreamEncryption(Model):
    def __int__(self):
        super(StreamEncryption, self).__init__(
            min_length={self.KeyId.__name__: 1},
            max_length={self.KeyId.__name__: 2048},
            allowed_values={self.EncryptionType.__name__: ["KMS"]},
            required_properties=ModelRequiredProperties.STREAM_ENCRYPTION
        )

    def EncryptionType(self, encryption_type: Union[str, AnyFn]):
        return self._set_field(self.EncryptionType.__name__, encryption_type)

    def KeyId(self, key_id: Union[str, AnyFn]):
        return self._set_field(self.KeyId.__name__, key_id)
