from crescent.core import Model
from .constants import AllowedValues, ModelRequiredProperties


class SseKmsEncryptedObjects(Model):
    def __init__(self):
        super(SseKmsEncryptedObjects, self).__init__(
            allowed_values={self.Status.__name__: AllowedValues.SSE_KMS_ENCRYPED_OBJECTS_STATUS},
            required_properties=ModelRequiredProperties.SSE_KMS_ENCRYPTED_OBJECTS
        )

    def Status(self, status: str):
        return self._set_field(self.Status.__name__, status)
