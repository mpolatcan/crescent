from crescent.core import Model, Validator
from .sse_kms_encrypted_objects import SseKmsEncryptedObjects
from .constants import RequiredProperties


class SourceSelectionCriteria(Model):
    @Validator.validate(type=SseKmsEncryptedObjects, required_properties=RequiredProperties.SSE_KMS_ENCRYPTED_OBJECTS)
    def SseKmsEncryptedObjects(self, value: SseKmsEncryptedObjects):
        return self._set_field(self.SseKmsEncryptedObjects.__name__, value.__to_dict__())
