from pyformation import PyformationResource


class MountTarget(PyformationResource):
    __TYPE = "AWS::EFS::MountTarget"

    def __init__(self, id: str):
        super(MountTarget, self).__init__(id, self.__TYPE)

    def FileSystemId(self, value: str):
        return self._set_property(self.FileSystemId.__name__, value)

    def IpAddress(self, value: str):
        return self._set_property(self.IpAddress.__name__, value)

    def SecurityGroups(self, *value: str):
        return self._set_property(self.SecurityGroups.__name__, list(value))

    def SubnetId(self, value: str):
        return self._set_property(self.SubnetId.__name__, value)
