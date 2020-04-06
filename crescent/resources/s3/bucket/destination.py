from crescent.core import Model
from .constants import AllowedValues, ModelRequiredProperties


class Destination(Model):
    def __init__(self):
        super(Destination, self).__init__(
            allowed_values={self.Format.__name__: AllowedValues.FORMAT},
            required_properties=ModelRequiredProperties.DESTINATION
        )

    def BucketAccountId(self, bucket_account_id: str):
        return self._set_field(self.BucketAccountId.__name__, bucket_account_id)

    def BucketArn(self, bucket_arn: str):
        return self._set_field(self.BucketArn.__name__, bucket_arn)

    def Format(self, format: str):
        return self._set_field(self.Format.__name__, format)

    def Prefix(self, prefix: str):
        return self._set_field(self.Prefix.__name__, prefix)
