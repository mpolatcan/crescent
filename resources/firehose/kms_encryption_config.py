from resources.shared import BaseModel


class KMSEncryptionConfig(BaseModel):
    __PROPERTY_AWS_KMS_KEY_ARN = "AWSKMSKeyARN"

    def aws_kms_key_arn(self, value: str):
        return self._add_field(self.__PROPERTY_AWS_KMS_KEY_ARN, value)
