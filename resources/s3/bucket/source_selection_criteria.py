from resources.shared import BaseModel
from resources.s3.bucket import SseKmsEncryptedObjects


class SourceSelectionCriteria(BaseModel):
    __PROPERTY_SSE_KMS_ENCRYPTED_OBJECTS = "SseKmsEncryptedObjects"

    def sse_kms_encrypted_objects(self, value: SseKmsEncryptedObjects):
        return self._add_field(self.__PROPERTY_SSE_KMS_ENCRYPTED_OBJECTS, value.create())
