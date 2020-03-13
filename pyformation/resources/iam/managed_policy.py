from pyformation.core import Resource, Validator


class ManagedPolicy(Resource):
    __TYPE = "AWS::IAM::ManagedPolicy"

    def __init__(self, id: str):
        super(ManagedPolicy, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def Description(self, value: str):
        return self._set_property(self.Description.__name__, value)

    @Validator.validate(type=str)
    def Groups(self, *value: str):
        return self._set_property(self.Groups.__name__, list(value))

    @Validator.validate(type=str)
    def ManagedPolicyName(self, value: str):
        return self._set_property(self.ManagedPolicyName.__name__, value)

    @Validator.validate(type=str)
    def Path(self, value: str):
        return self._set_property(self.Path.__name__, value)

    @Validator.validate(type=str)
    def Roles(self, *value: str):
        return self._set_property(self.Roles.__name__, list(value))

    @Validator.validate(type=str)
    def Users(self, *value: str):
        return self._set_property(self.Users.__name__, list(value))
