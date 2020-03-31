from crescent.core import Resource, Tag, Validator
from .policy_model import PolicyModel
from .login_profile import LoginProfile
from .arn import PolicyArn
from .constants import AllowedValues, ModelRequiredProperties


class User(Resource):
    __TYPE = "AWS::IAM::User"

    def __init__(self, id: str):
        super(User, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def Groups(self, *groups: str):
        return self._set_property(self.Groups.__name__, list(groups))

    @Validator.validate(type=LoginProfile, required_properties=ModelRequiredProperties.LOGIN_PROFILE)
    def LoginProfile(self, login_profile: LoginProfile):
        return self._set_property(self.LoginProfile.__name__, login_profile.__to_dict__())

    @Validator.validate(type=PolicyArn, allowed_values=AllowedValues.MANAGED_POLICY_ARNS)
    def ManagedPolicyArns(self, *managed_policy_arns: str):
        return self._set_property(self.ManagedPolicyArns.__name__, list(managed_policy_arns))

    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"(\u002F)|(\u002F[\u0021-\u007F]+\u002F)")
    def Path(self, path: str):
        return self._set_property(self.Path.__name__, path)

    @Validator.validate(type=str)
    def PermissionBoundary(self, permission_boundary: str):
        return self._set_property(self.PermissionBoundary.__name__, permission_boundary)

    @Validator.validate(type=PolicyModel, required_properties=ModelRequiredProperties.POLICY_MODEL)
    def Policies(self, *policies: PolicyModel):
        return self._set_property(self.Policies.__name__, [pm.__to_dict__() for pm in list(policies)])

    @Validator.validate(type=Tag, max_length=50)
    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))

    @Validator.validate(type=str)
    def UserName(self, user_name: str):
        return self._set_property(self.UserName.__name__, user_name)
