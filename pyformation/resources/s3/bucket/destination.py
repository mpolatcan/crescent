from pyformation.core import Model, Validator


class Destination(Model):
    @Validator.validate(type=str)
    def BucketAccountId(self, value: str):
        return self._set_field(self.BucketAccountId.__name__, value)

    @Validator.validate(type=str)
    def BucketArn(self, value: str):
        return self._set_field(self.BucketArn.__name__, value)

    @Validator.validate(type=str)
    def Format(self, value: str):
        return self._set_field(self.Format.__name__, value)

    @Validator.validate(type=str)
    def Prefix(self, value: str):
        return self._set_field(self.Prefix.__name__, value)
