from pyformation import PyformationModel


class StreamEncryption(PyformationModel):
    def EncryptionType(self, value: str):
        return self._set_field(self.EncryptionType.__name__, value)

    def KeyId(self, value: str):
        return self._set_field(self.KeyId.__name__, value)
