from crescent.core import Resource, Validator


class InstanceProfile(Resource):
    __TYPE = "AWS::IAM::InstanceProfile"

    def __init__(self, id: str):
        super(InstanceProfile, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str, min_length=1, max_length=128, pattern=r"[\w+=,.@-]+")
    def InstanceProfileName(self, value: str):
        return self._set_property(self.InstanceProfileName.__name__, value)

    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"(\u002F)|(\u002F[\u0021-\u007F]+\u002F)")
    def Path(self, value: str):
        return self._set_property(self.Path.__name__, value)

    @Validator.validate(type=str)
    def Roles(self, *value: str):
        return self._set_property(self.Roles.__name__, list(value))
