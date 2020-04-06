from crescent.core import Model
from .sse_kms_encrypted_objects import SseKmsEncryptedObjects
from .constants import ModelRequiredProperties


class SourceSelectionCriteria(Model):
    def __init__(self):
        super(SourceSelectionCriteria, self).__init__(required_properties=ModelRequiredProperties.SOURCE_SELECTION_CRITERIA)

    def SseKmsEncryptedObjects(self, sse_kms_encrypted_objects: SseKmsEncryptedObjects):
        return self._set_field(self.SseKmsEncryptedObjects.__name__, sse_kms_encrypted_objects)
