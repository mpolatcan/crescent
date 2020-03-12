from pyformation import PyformationResource


class ManagedPolicy(PyformationResource):
    __TYPE = "AWS::IAM::ManagedPolicy"

    def __init__(self, id: str):
        super(ManagedPolicy, self).__init__(id, self.__TYPE)

    def Description(self, value: str):
        return self._set_property(self.Description.__name__, value)

    def Groups(self, *value: str):
        return self._set_property(self.Groups.__name__, list(value))

    def ManagedPolicyName(self, value: str):
        return self._set_property(self.ManagedPolicyName.__name__, value)

    def Path(self, value: str):
        return self._set_property(self.Path.__name__, value)

    def Roles(self, *value: str):
        return self._set_property(self.Roles.__name__, list(value))

    def Users(self, *value: str):
        return self._set_property(self.Users.__name__, list(value))
