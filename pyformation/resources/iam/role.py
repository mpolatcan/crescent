from pyformation.core import Resource, Tag, Validator
from .policy_model import PolicyModel


class Role(Resource):
    __TYPE = "AWS::IAM:Role"

    def __init__(self, id: str):
        super(Role, self).__init__(id, self.__TYPE)

    @Validator.validate(type=dict)
    def AssumeRolePolicyDocument(self, value: dict):
        return self._set_property(self.AssumeRolePolicyDocument.__name__, value)

    @Validator.validate(type=str)
    def Description(self, value: str):
        return self._set_property(self.Description.__name__, value)

    @Validator.validate(type=str)
    def ManagedPolicyArns(self, *value: str):
        return self._set_property(self.ManagedPolicyArns.__name__, list(value))

    @Validator.validate(type=int)
    def MaxSessionDuration(self, value: int):
        return self._set_property(self.MaxSessionDuration.__name__, value)

    @Validator.validate(type=str)
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

    @Validator.validate(type=Tag)
    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))
