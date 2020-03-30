from crescent.core import Resource, Tag, Validator
from .policy_model import PolicyModel
from .constants import ModelRequiredProperties


class Role(Resource):
    __TYPE = "AWS::IAM:Role"

    def __init__(self, id: str):
        super(Role, self).__init__(id, self.__TYPE)

    @Validator.validate(type=dict)
    def AssumeRolePolicyDocument(self, assume_role_policy_document: dict):
        return self._set_property(self.AssumeRolePolicyDocument.__name__, assume_role_policy_document)

    @Validator.validate(type=str, max_length=1000, pattern=r"[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*")
    def Description(self, description: str):
        return self._set_property(self.Description.__name__, description)

    @Validator.validate(type=str)
    def ManagedPolicyArns(self, *managed_policy_arns: str):
        return self._set_property(self.ManagedPolicyArns.__name__, list(managed_policy_arns))

    @Validator.validate(type=int, min_value=3600, maximum=43200)
    def MaxSessionDuration(self, max_session_duration: int):
        return self._set_property(self.MaxSessionDuration.__name__, max_session_duration)

    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"(\u002F)|(\u002F[\u0021-\u007F]+\u002F)")
    def Path(self, path: str):
        return self._set_property(self.Path.__name__, path)

    @Validator.validate(type=str)
    def PermissionBoundary(self, permission_boundary: str):
        return self._set_property(self.PermissionBoundary.__name__, permission_boundary)

    @Validator.validate(type=PolicyModel, required_properties=ModelRequiredProperties.POLICY_MODEL)
    def Policies(self, *policies: PolicyModel):
        return self._set_property(self.Policies.__name__, [pm.__to_dict__() for pm in list(policies)])

    @Validator.validate(type=str)
    def RoleName(self, role_name: str):
        return self._set_property(self.RoleName.__name__, role_name)

    @Validator.validate(type=Tag, min_length=50)
    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))
