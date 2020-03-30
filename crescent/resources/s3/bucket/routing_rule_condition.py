from crescent.core import Model, Validator


class RoutingRuleCondition(Model):
    @Validator.validate(type=str)
    def HttpErrorCodeReturnedEquals(self, http_error_code_returned_equals: str):
        return self._set_field(self.HttpErrorCodeReturnedEquals.__name__, http_error_code_returned_equals)

    @Validator.validate(type=str)
    def KeyPrefixEquals(self, key_prefix_equals: str):
        return self._set_field(self.KeyPrefixEquals.__name__, key_prefix_equals)
