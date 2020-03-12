from pyformation import PyformationModel


class ServerSideEncryptionByDefault(PyformationModel):
    def KMSMasterKeyId(self, value: str):
        return self._set_field(self.KMSMasterKeyId.__name__, value)

    def SSEAlgorithm(self, value: str):
        return self._set_field(self.SSEAlgorithm.__name__, value)
