from pyformation import PyformationModel


class RoutingRuleCondition(PyformationModel):
    def HttpErrorCodeReturnedEquals(self, value: str):
        return self._set_field(self.HttpErrorCodeReturnedEquals.__name__, value)

    def KeyPrefixEquals(self, value: str):
        return self._set_field(self.KeyPrefixEquals.__name__, value)
