from crescent.core import Model, Validator
from .constants import AllowedValues


class ServerSideEncryptionByDefault(Model):
    @Validator.validate(type=str)
    def KMSMasterKeyId(self, kms_master_key_id: str):
        return self._set_field(self.KMSMasterKeyId.__name__, kms_master_key_id)

    @Validator.validate(type=str, allowed_values=AllowedValues.SSE_BY_DEFAULT_SSE_ALGORITHM)
    def SSEAlgorithm(self, sse_algorithm: str):
        return self._set_field(self.SSEAlgorithm.__name__, sse_algorithm)
