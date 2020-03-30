from crescent.core import Resource, Validator


class MountTarget(Resource):
    __TYPE = "AWS::EFS::MountTarget"

    def __init__(self, id: str):
        super(MountTarget, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def FileSystemId(self, file_system_id: str):
        return self._set_property(self.FileSystemId.__name__, file_system_id)

    @Validator.validate(type=str)
    def IpAddress(self, ip_address: str):
        return self._set_property(self.IpAddress.__name__, ip_address)

    @Validator.validate(type=str, max_length=5)
    def SecurityGroups(self, *security_groups: str):
        return self._set_property(self.SecurityGroups.__name__, list(security_groups))

    @Validator.validate(type=str)
    def SubnetId(self, subnet_id: str):
        return self._set_property(self.SubnetId.__name__, subnet_id)
