from resources.shared.base_model import BaseModel


class ServerSideEncryptionByDefault(BaseModel):
    __PROPERTY_KMS_MASTER_KEY_ID = "KMSMasterKeyId"
    __PROPERTY_SSE_ALGORITHM = "SSEAlgorithm"

    def kms_master_key_id(self, value: str):
        return self._add_field(self.__PROPERTY_KMS_MASTER_KEY_ID, value)

    def sse_algorithm(self, value: str):
        return self._add_field(self.__PROPERTY_SSE_ALGORITHM, value)
