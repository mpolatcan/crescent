from crescent.core import Resource, Validator


class InstanceProfile(Resource):
    __TYPE = "AWS::IAM::InstanceProfile"

    def __init__(self, id: str):
        super(InstanceProfile, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str, min_length=1, max_length=128, pattern=r"[\w+=,.@-]+")
    def InstanceProfileName(self, instance_profile_name: str):
        return self._set_property(self.InstanceProfileName.__name__, instance_profile_name)

    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"(\u002F)|(\u002F[\u0021-\u007F]+\u002F)")
    def Path(self, path: str):
        return self._set_property(self.Path.__name__, path)

    @Validator.validate(type=str)
    def Roles(self, *roles: str):
        return self._set_property(self.Roles.__name__, list(roles))
