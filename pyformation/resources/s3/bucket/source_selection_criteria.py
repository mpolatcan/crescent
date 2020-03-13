from pyformation.core import Model, Validator
from .sse_kms_encrypted_objects import SseKmsEncryptedObjects


class SourceSelectionCriteria(Model):
    __PROPERTY_SSE_KMS_ENCRYPTED_OBJECTS = "SseKmsEncryptedObjects"

    @Validator.validate(type=SseKmsEncryptedObjects)
    def SseKmsEncryptedObjects(self, value: SseKmsEncryptedObjects):
        return self._set_field(self.SseKmsEncryptedObjects.__name__, value.__to_dict__())
