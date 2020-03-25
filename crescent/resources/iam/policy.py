from crescent.core import Resource, Validator


class Policy(Resource):
    __TYPE = "AWS::IAM::Policy"

    def __init__(self, id: str):
        super(Policy, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str, min_length=1, max_length=128, pattern=r"[\w+=,.@-]+")
    def Groups(self, *value: str):
        return self._set_property(self.Groups.__name__, list(value))

    @Validator.validate(type=dict, min_length=1, max_length=131072, pattern=r"[\u0009\u000A\u000D\u0020-\u00FF]+")
    def PolicyDocument(self, value: dict):
        return self._set_property(self.PolicyDocument.__name__, value)

    @Validator.validate(type=str, min_length=1, max_length=128, pattern=r"[\w+=,.@-]+")
    def PolicyName(self, value: str):
        return self._set_property(self.PolicyName.__name__, value)

    @Validator.validate(type=str)
    def Roles(self, *value: str):
        return self._set_property(self.Roles.__name__, list(value))

    @Validator.validate(type=str, min_length=1, max_length=128, pattern=r"[\w+=,.@-]+")
    def Users(self, *value: str):
        return self._set_property(self.Users.__name__, list(value))
