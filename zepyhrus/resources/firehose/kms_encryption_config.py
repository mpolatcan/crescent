from zepyhrus.core import Model, Validator


class KMSEncryptionConfig(Model):
    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"arn:.*")
    def AWSKMSKeyARN(self, value: str):
        return self._set_field(self.AWSKMSKeyARN.__name__, value)
