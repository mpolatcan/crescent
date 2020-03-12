from pyformation import PyformationResource


class Policy(PyformationResource):
    __TYPE = "AWS::IAM::Policy"

    def __init__(self, id: str):
        super(Policy, self).__init__(id, self.__TYPE)

    def Groups(self, *value: str):
        return self._set_property(self.Groups.__name__, list(value))

    def PolicyDocument(self, value: dict):
        return self._set_property(self.PolicyDocument.__name__, value)

    def PolicyName(self, value: str):
        return self._set_property(self.PolicyName.__name__, value)

    def Roles(self, *value: str):
        return self._set_property(self.Roles.__name__, list(value))

    def Users(self, *value: str):
        return self._set_property(self.Users.__name__, list(value))
