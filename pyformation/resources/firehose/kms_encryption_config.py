from pyformation.core import Model, Validator


class KMSEncryptionConfig(Model):
    @Validator.validate(type=str)
    def AWSKMSKeyARN(self, value: str):
        return self._set_field(self.AWSKMSKeyARN.__name__, value)
