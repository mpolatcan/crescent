from crescent.core import Model, Validator


class DBInstanceRole(Model):
    @Validator.validate(type=str)
    def FeatureName(self, value: str):
        return self._set_field(self.FeatureName.__name__, value)

    @Validator.validate(type=str)
    def RoleArn(self, value: str):
        return self._set_field(self.RoleArn.__name__, value)
