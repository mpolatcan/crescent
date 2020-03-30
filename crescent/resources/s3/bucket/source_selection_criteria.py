from crescent.core import Model, Validator
from .sse_kms_encrypted_objects import SseKmsEncryptedObjects
from .constants import ModelRequiredProperties


class SourceSelectionCriteria(Model):
    @Validator.validate(type=SseKmsEncryptedObjects, required_properties=ModelRequiredProperties.SSE_KMS_ENCRYPTED_OBJECTS)
    def SseKmsEncryptedObjects(self, sse_kms_encrypted_objects: SseKmsEncryptedObjects):
        return self._set_field(self.SseKmsEncryptedObjects.__name__, sse_kms_encrypted_objects.__to_dict__())
