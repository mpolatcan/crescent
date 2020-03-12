from pyformation import PyformationResource, Tag
from .policy_model import PolicyModel
from .login_profile import LoginProfile


class User(PyformationResource):
    __TYPE = "AWS::IAM::User"

    def __init__(self, id: str):
        super(User, self).__init__(id, self.__TYPE)

    def Groups(self, *value: str):
        return self._set_property(self.Groups.__name__, list(value))

    def LoginProfile(self, value: LoginProfile):
        return self._set_property(self.LoginProfile.__name__, value.__to_dict__())

    def ManagedPolicyArns(self, *value: str):
        return self._set_property(self.ManagedPolicyArns.__name__, list(value))

    def Path(self, value: str):
        return self._set_property(self.Path.__name__, value)

    def PermissionBoundary(self, value: str):
        return self._set_property(self.PermissionBoundary.__name__, value)

    def Policies(self, *value: PolicyModel):
        return self._set_property(self.Policies.__name__, [pm.__to_dict__() for pm in list(value)])

    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))

    def UserName(self, value: str):
        return self._set_property(self.UserName.__name__, value)
