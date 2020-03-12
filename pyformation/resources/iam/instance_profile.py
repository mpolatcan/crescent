from pyformation import PyformationResource


class InstanceProfile(PyformationResource):
    __TYPE = "AWS::IAM::InstanceProfile"

    def __init__(self, id: str):
        super(InstanceProfile, self).__init__(id, self.__TYPE)

    def InstanceProfileName(self, value: str):
        return self._set_property(self.InstanceProfileName.__name__, value)

    def Path(self, value: str):
        return self._set_property(self.Path.__name__, value)

    def Roles(self, *value: str):
        return self._set_property(self.Roles.__name__, list(value))
