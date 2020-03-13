from pyformation.core import Resource, Validator


class MountTarget(Resource):
    __TYPE = "AWS::EFS::MountTarget"

    def __init__(self, id: str):
        super(MountTarget, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def FileSystemId(self, value: str):
        return self._set_property(self.FileSystemId.__name__, value)

    @Validator.validate(type=str)
    def IpAddress(self, value: str):
        return self._set_property(self.IpAddress.__name__, value)

    @Validator.validate(type=str)
    def SecurityGroups(self, *value: str):
        return self._set_property(self.SecurityGroups.__name__, list(value))

    @Validator.validate(type=str)
    def SubnetId(self, value: str):
        return self._set_property(self.SubnetId.__name__, value)
