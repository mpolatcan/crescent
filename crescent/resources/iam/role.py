from crescent.core import Resource, Tag
from crescent.functions import AnyFn
from .policy_model import PolicyModel
from .constants import AllowedValues, ResourceRequiredProperties
from .arn import PolicyArn
from typing import Union


class Role(Resource):
    __TYPE = "AWS::IAM:Role"

    def __init__(self, id: str):
        super(Role, self).__init__(
            id=id,
            type=self.__TYPE,
            min_value={self.MaxSessionDuration.__name__: 3600},
            max_value={self.MaxSessionDuration.__name__: 43200},
            min_length={self.Path.__name__: 1},
            max_length={self.Description.__name__: 1000,
                        self.Path.__name__: 512,
                        self.Tags.__name__: 50},
            pattern={self.Description.__name__: r"[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*",
                     self.Path.__name__: r"(\u002F)|(\u002F[\u0021-\u007F]+\u002F)"},
            allowed_values={self.ManagedPolicyArns.__name__: AllowedValues.MANAGED_POLICY_ARNS},
            required_properties=ResourceRequiredProperties.ROLE
        )

    def AssumeRolePolicyDocument(self, assume_role_policy_document: Union[dict, AnyFn]):
        return self._set_property(self.AssumeRolePolicyDocument.__name__, assume_role_policy_document)

    def Description(self, description: Union[str, AnyFn]):
        return self._set_property(self.Description.__name__, description)

    def ManagedPolicyArns(self, *managed_policy_arns: PolicyArn):
        return self._set_property(self.ManagedPolicyArns.__name__, list(managed_policy_arns))

    def MaxSessionDuration(self, max_session_duration: Union[int, AnyFn]):
        return self._set_property(self.MaxSessionDuration.__name__, max_session_duration)

    def Path(self, path: Union[str, AnyFn]):
        return self._set_property(self.Path.__name__, path)

    def PermissionBoundary(self, permission_boundary: Union[str, AnyFn]):
        return self._set_property(self.PermissionBoundary.__name__, permission_boundary)

    def Policies(self, *policies: PolicyModel):
        return self._set_property(self.Policies.__name__, list(policies))

    def RoleName(self, role_name: Union[str, AnyFn]):
        return self._set_property(self.RoleName.__name__, role_name)

    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))
