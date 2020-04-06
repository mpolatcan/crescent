from crescent.core import Model
from .constants import AllowedValues, ModelRequiredProperties


class ServerSideEncryptionByDefault(Model):
    def __init__(self):
        super(ServerSideEncryptionByDefault, self).__init__(
            allowed_values={self.SSEAlgorithm.__name__: AllowedValues.SSE_BY_DEFAULT_SSE_ALGORITHM},
            required_properties=ModelRequiredProperties.SERVER_SIDE_ENCRYPTION_BY_DEFAULT
        )

    def KMSMasterKeyId(self, kms_master_key_id: str):
        return self._set_field(self.KMSMasterKeyId.__name__, kms_master_key_id)

    def SSEAlgorithm(self, sse_algorithm: str):
        return self._set_field(self.SSEAlgorithm.__name__, sse_algorithm)
