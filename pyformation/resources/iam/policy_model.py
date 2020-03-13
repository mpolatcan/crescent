from pyformation.core import Model, Validator


class PolicyModel(Model):
    @Validator.validate(type=dict)
    def PolicyDocument(self, value: dict):
        return self._set_field(self.PolicyDocument.__name__, value)

    @Validator.validate(type=str)
    def PolicyName(self, value: str):
        return self._set_field(self.PolicyName.__name__, value)
