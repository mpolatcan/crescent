from pyformation.core import Resource, Validator


class InstanceProfile(Resource):
    __TYPE = "AWS::IAM::InstanceProfile"

    def __init__(self, id: str):
        super(InstanceProfile, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def InstanceProfileName(self, value: str):
        return self._set_property(self.InstanceProfileName.__name__, value)

    @Validator.validate(type=str)
    def Path(self, value: str):
        return self._set_property(self.Path.__name__, value)

    @Validator.validate(type=str)
    def Roles(self, *value: str):
        return self._set_property(self.Roles.__name__, list(value))
