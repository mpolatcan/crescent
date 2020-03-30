from crescent.core import Model, Validator


class DBInstanceRole(Model):
    @Validator.validate(type=str)
    def FeatureName(self, feature_name: str):
        return self._set_field(self.FeatureName.__name__, feature_name)

    @Validator.validate(type=str)
    def RoleArn(self, role_arn: str):
        return self._set_field(self.RoleArn.__name__, role_arn)
