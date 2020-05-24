from crescent.core import Model
from .constants import ModelRequiredProperties, AllowedValues


class SSESpecification(Model):
    def __init__(self):
        super(SSESpecification, self).__init__(
            allowed_values={self.SSEType.__name__: AllowedValues.SSE_TYPE},
            required_properties=ModelRequiredProperties.SSE_SPECIFICATION
        )

    def KMSMasterKeyId(self, kms_master_key_id: str):
        return self._set_field(self.KMSMasterKeyId.__name__, kms_master_key_id)

    def SSEEnabled(self, sse_enabled: bool):
        return self._set_field(self.SSEEnabled.__name__, sse_enabled)

    def SSEType(self, sse_type: str):
        return self._set_field(self.SSEType.__name__, sse_type)