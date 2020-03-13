from pyformation.core import Resource, Validator


class Policy(Resource):
    __TYPE = "AWS::IAM::Policy"

    def __init__(self, id: str):
        super(Policy, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def Groups(self, *value: str):
        return self._set_property(self.Groups.__name__, list(value))

    @Validator.validate(type=dict)
    def PolicyDocument(self, value: dict):
        return self._set_property(self.PolicyDocument.__name__, value)

    @Validator.validate(type=str)
    def PolicyName(self, value: str):
        return self._set_property(self.PolicyName.__name__, value)

    @Validator.validate(type=str)
    def Roles(self, *value: str):
        return self._set_property(self.Roles.__name__, list(value))

    @Validator.validate(type=str)
    def Users(self, *value: str):
        return self._set_property(self.Users.__name__, list(value))
