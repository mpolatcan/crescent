from pyformation.core import Model, Validator
from .constants import AllowedValues


class SseKmsEncryptedObjects(Model):
    @Validator.validate(type=str, allowed_values=AllowedValues.SSE_KMS_ENCRYPED_OBJECTS_STATUS)
    def Status(self, value: str):
        return self._set_field(self.Status.__name__, value)
