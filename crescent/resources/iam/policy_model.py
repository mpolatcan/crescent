from crescent.core import Model, Validator


class PolicyModel(Model):
    @Validator.validate(type=dict, min_length=1, max_length=131072, pattern=r"[\u0009\u000A\u000D\u0020-\u00FF]+")
    def PolicyDocument(self, policy_document: dict):
        return self._set_field(self.PolicyDocument.__name__, policy_document)

    @Validator.validate(type=str, min_length=1, max_length=128, pattern=r"[\w+=,.@-]+")
    def PolicyName(self, policy_name: str):
        return self._set_field(self.PolicyName.__name__, policy_name)
