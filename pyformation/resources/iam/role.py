from pyformation.core import Resource, Tag, Validator
from .policy_model import PolicyModel


class Role(Resource):
    __TYPE = "AWS::IAM:Role"

    def __init__(self, id: str):
        super(Role, self).__init__(id, self.__TYPE)

    @Validator.validate(type=dict)
    def AssumeRolePolicyDocument(self, value: dict):
        return self._set_property(self.AssumeRolePolicyDocument.__name__, value)

    @Validator.validate(type=str, max_length=1000, pattern="[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*")
    def Description(self, value: str):
        return self._set_property(self.Description.__name__, value)

    @Validator.validate(type=str)
    def ManagedPolicyArns(self, *value: str):
        return self._set_property(self.ManagedPolicyArns.__name__, list(value))

    @Validator.validate(type=int, min_value=3600, maximum=43200)
    def MaxSessionDuration(self, value: int):
        return self._set_property(self.MaxSessionDuration.__name__, value)

    @Validator.validate(type=str, min_length=1, max_length=512, pattern="(\u002F)|(\u002F[\u0021-\u007F]+\u002F)")
    def Path(self, value: str):
        return self._set_property(self.Path.__name__, value)

    @Validator.validate(type=str)
    def PermissionBoundary(self, value: str):
        return self._set_property(self.PermissionBoundary.__name__, value)

    @Validator.validate(type=PolicyModel)
    def Policies(self, *value: PolicyModel):
        return self._set_property(self.Policies.__name__, [pm.__to_dict__() for pm in list(value)])

    @Validator.validate(type=str)
    def RoleName(self, value: str):
        return self._set_property(self.RoleName.__name__, value)

    @Validator.validate(type=Tag, min_length=50)
    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))
