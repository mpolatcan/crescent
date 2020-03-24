from zepyhrus.core import Model, Validator


class PublicAccessBlockConfiguration(Model):
    @Validator.validate(type=bool)
    def BlockPublicAcls(self, value: bool):
        return self._set_field(self.BlockPublicAcls.__name__, value)

    @Validator.validate(type=bool)
    def BlockPublicPolicy(self, value: bool):
        return self._set_field(self.BlockPublicPolicy.__name__, value)

    @Validator.validate(type=bool)
    def IgnorePublicAcls(self, value: bool):
        return self._set_field(self.IgnorePublicAcls.__name__, value)

    @Validator.validate(type=bool)
    def RestrictPublicBuckets(self, value: bool):
        return self._set_field(self.RestrictPublicBuckets.__name__, value)
