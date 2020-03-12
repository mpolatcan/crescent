from pyformation import PyformationModel


class KMSEncryptionConfig(PyformationModel):
    def AWSKMSKeyARN(self, value: str):
        return self._set_field(self.AWSKMSKeyARN.__name__, value)
