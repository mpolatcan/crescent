from crescent.core import Model, Validator
from .constants import AllowedValues


class Destination(Model):
    @Validator.validate(type=str)
    def BucketAccountId(self, bucket_account_id: str):
        return self._set_field(self.BucketAccountId.__name__, bucket_account_id)

    @Validator.validate(type=str)
    def BucketArn(self, bucket_arn: str):
        return self._set_field(self.BucketArn.__name__, bucket_arn)

    @Validator.validate(type=str, allowed_values=AllowedValues.FORMAT)
    def Format(self, format: str):
        return self._set_field(self.Format.__name__, format)

    @Validator.validate(type=str)
    def Prefix(self, prefix: str):
        return self._set_field(self.Prefix.__name__, prefix)
