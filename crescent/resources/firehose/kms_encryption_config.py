from crescent.core import Model, Validator


class KMSEncryptionConfig(Model):
    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"arn:.*")
    def AWSKMSKeyARN(self, aws_kms_key_arn: str):
        return self._set_field(self.AWSKMSKeyARN.__name__, aws_kms_key_arn)
