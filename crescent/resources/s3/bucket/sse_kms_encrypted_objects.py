from crescent.core import Model
from crescent.functions import AnyFn
from .constants import AllowedValues, ModelRequiredProperties
from typing import Union


class SseKmsEncryptedObjects(Model):
    def __init__(self):
        super(SseKmsEncryptedObjects, self).__init__(
            allowed_values={self.Status.__name__: AllowedValues.SSE_KMS_ENCRYPED_OBJECTS_STATUS},
            required_properties=ModelRequiredProperties.SSE_KMS_ENCRYPTED_OBJECTS
        )

    def Status(self, status: Union[str, AnyFn]):
        return self._set_field(self.Status.__name__, status)
