from pyformation.core import Model, Validator
from .constants import AllowedValues


class ServerSideEncryptionByDefault(Model):
    @Validator.validate(type=str)
    def KMSMasterKeyId(self, value: str):
        return self._set_field(self.KMSMasterKeyId.__name__, value)

    @Validator.validate(type=str, allowed_values=AllowedValues.SSE_BY_DEFAULT_SSE_ALGORITHM)
    def SSEAlgorithm(self, value: str):
        return self._set_field(self.SSEAlgorithm.__name__, value)
