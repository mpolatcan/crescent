from zepyhrus.core import Model, Validator


class PolicyModel(Model):
    @Validator.validate(type=dict, min_length=1, max_length=131072, pattern="[\u0009\u000A\u000D\u0020-\u00FF]+")
    def PolicyDocument(self, value: dict):
        return self._set_field(self.PolicyDocument.__name__, value)

    @Validator.validate(type=str, min_length=1, max_length=128, pattern="[\w+=,.@-]+")
    def PolicyName(self, value: str):
        return self._set_field(self.PolicyName.__name__, value)
