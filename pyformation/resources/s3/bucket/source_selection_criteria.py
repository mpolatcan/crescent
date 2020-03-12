from pyformation import PyformationModel
from .sse_kms_encrypted_objects import SseKmsEncryptedObjects


class SourceSelectionCriteria(PyformationModel):
    __PROPERTY_SSE_KMS_ENCRYPTED_OBJECTS = "SseKmsEncryptedObjects"

    def SseKmsEncryptedObjects(self, value: SseKmsEncryptedObjects):
        return self._set_field(self.SseKmsEncryptedObjects.__name__, value.__to_dict__())
