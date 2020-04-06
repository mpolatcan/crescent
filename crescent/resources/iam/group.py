from crescent.core import Resource
from .policy_model import PolicyModel
from .constants import AllowedValues
from .arn import PolicyArn


class Group(Resource):
    __TYPE = "AWS::IAM::Group"

    def __init__(self, id: str):
        super(Group, self).__init__(
            id=id,
            type=self.__TYPE,
            min_length={self.Path.__name__: 1},
            max_length={self.Path.__name__: 512},
            pattern={self.Path.__name__: r"(\u002F)|(\u002F[\u0021-\u007F]+\u002F)"},
            allowed_values={self.ManagedPolicyArns.__name__: AllowedValues.MANAGED_POLICY_ARNS}
        )

    def GroupName(self, group_name: str):
        return self._set_property(self.GroupName.__name__, group_name)

    def ManagedPolicyArns(self, *managed_policy_arns: PolicyArn):
        return self._set_property(self.ManagedPolicyArns.__name__, list(managed_policy_arns))

    def Path(self, path: str):
        return self._set_property(self.Path.__name__, path)

    def Policies(self, *policies: PolicyModel):
        return self._set_property(self.Policies.__name__, list(policies))

