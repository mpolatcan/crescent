from pyformation import PyformationResource, Tag
from .policy_model import PolicyModel


class Role(PyformationResource):
    __TYPE = "AWS::IAM:Role"

    def __init__(self, id: str):
        super(Role, self).__init__(id, self.__TYPE)

    def AssumeRolePolicyDocument(self, value: dict):
        return self._set_property(self.AssumeRolePolicyDocument.__name__, value)

    def Description(self, value: str):
        return self._set_property(self.Description.__name__, value)

    def ManagedPolicyArns(self, *value: str):
        return self._set_property(self.ManagedPolicyArns.__name__, list(value))

    def MaxSessionDuration(self, value: int):
        return self._set_property(self.MaxSessionDuration.__name__, value)

    def Path(self, value: str):
        return self._set_property(self.Path.__name__, value)

    def PermissionBoundary(self, value: str):
        return self._set_property(self.PermissionBoundary.__name__, value)

    def Policies(self, *value: PolicyModel):
        return self._set_property(self.Policies.__name__, [pm.__to_dict__() for pm in list(value)])

    def RoleName(self, value: str):
        return self._set_property(self.RoleName.__name__, value)

    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))
