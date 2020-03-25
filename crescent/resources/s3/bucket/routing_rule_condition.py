from crescent.core import Model, Validator


class RoutingRuleCondition(Model):
    @Validator.validate(type=str)
    def HttpErrorCodeReturnedEquals(self, value: str):
        return self._set_field(self.HttpErrorCodeReturnedEquals.__name__, value)

    @Validator.validate(type=str)
    def KeyPrefixEquals(self, value: str):
        return self._set_field(self.KeyPrefixEquals.__name__, value)
