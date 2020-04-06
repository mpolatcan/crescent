from crescent.core import Resource, Tag
from .policy_model import PolicyModel
from .login_profile import LoginProfile
from .arn import PolicyArn
from .constants import AllowedValues


class User(Resource):
    __TYPE = "AWS::IAM::User"

    def __init__(self, id: str):
        super(User, self).__init__(
            id=id,
            type=self.__TYPE,
            min_length={self.Path.__name__: 1},
            max_length={self.Path.__name__: 512,
                        self.Tags.__name__: 50},
            pattern={self.Path.__name__: r"(\u002F)|(\u002F[\u0021-\u007F]+\u002F)"},
            allowed_values={self.ManagedPolicyArns.__name__: AllowedValues.MANAGED_POLICY_ARNS}
        )

    def Groups(self, *groups: str):
        return self._set_property(self.Groups.__name__, list(groups))

    def LoginProfile(self, login_profile: LoginProfile):
        return self._set_property(self.LoginProfile.__name__, login_profile)

    def ManagedPolicyArns(self, *managed_policy_arns: PolicyArn):
        return self._set_property(self.ManagedPolicyArns.__name__, list(managed_policy_arns))

    def Path(self, path: str):
        return self._set_property(self.Path.__name__, path)

    def PermissionBoundary(self, permission_boundary: str):
        return self._set_property(self.PermissionBoundary.__name__, permission_boundary)

    def Policies(self, *policies: PolicyModel):
        return self._set_property(self.Policies.__name__, list(policies))

    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))

    def UserName(self, user_name: str):
        return self._set_property(self.UserName.__name__, user_name)
