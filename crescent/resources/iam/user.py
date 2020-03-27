from crescent.core import Resource, Tag, Validator
from .policy_model import PolicyModel
from .login_profile import LoginProfile
from .constants import ModelRequiredProperties


class User(Resource):
    __TYPE = "AWS::IAM::User"

    def __init__(self, id: str):
        super(User, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def Groups(self, *value: str):
        return self._set_property(self.Groups.__name__, list(value))

    @Validator.validate(type=LoginProfile, required_properties=ModelRequiredProperties.LOGIN_PROFILE)
    def LoginProfile(self, value: LoginProfile):
        return self._set_property(self.LoginProfile.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def ManagedPolicyArns(self, *value: str):
        return self._set_property(self.ManagedPolicyArns.__name__, list(value))

    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"(\u002F)|(\u002F[\u0021-\u007F]+\u002F)")
    def Path(self, value: str):
        return self._set_property(self.Path.__name__, value)

    @Validator.validate(type=str)
    def PermissionBoundary(self, value: str):
        return self._set_property(self.PermissionBoundary.__name__, value)

    @Validator.validate(type=PolicyModel, required_properties=ModelRequiredProperties.POLICY_MODEL)
    def Policies(self, *value: PolicyModel):
        return self._set_property(self.Policies.__name__, [pm.__to_dict__() for pm in list(value)])

    @Validator.validate(type=Tag, max_length=50)
    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))

    @Validator.validate(type=str)
    def UserName(self, value: str):
        return self._set_property(self.UserName.__name__, value)
