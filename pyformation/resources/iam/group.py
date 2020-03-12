from pyformation import PyformationResource
from .policy_model import PolicyModel


class Group(PyformationResource):
    __TYPE = "AWS::IAM::Group"

    def __init__(self, id: str):
        super(Group, self).__init__(id, self.__TYPE)

    def GroupName(self, value: str):
        return self._set_property(self.GroupName.__name__, value)

    def ManagedPolicyArns(self, *value: str):
        return self._set_property(self.ManagedPolicyArns.__name__, list(value))

    def Path(self, value: str):
        return self._set_property(self.Path.__name__, value)

    def Policies(self, *value: PolicyModel):
        return self._set_property(self.Policies.__name__, [pm.__to_dict__() for pm in list(value)])

