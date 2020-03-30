from crescent.core import Resource, Validator
from .policy_model import PolicyModel
from .constants import ModelRequiredProperties


class Group(Resource):
    __TYPE = "AWS::IAM::Group"

    def __init__(self, id: str):
        super(Group, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def GroupName(self, group_name: str):
        return self._set_property(self.GroupName.__name__, group_name)

    @Validator.validate(type=str)
    def ManagedPolicyArns(self, *managed_policy_arns: str):
        return self._set_property(self.ManagedPolicyArns.__name__, list(managed_policy_arns))

    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"(\u002F)|(\u002F[\u0021-\u007F]+\u002F)")
    def Path(self, path: str):
        return self._set_property(self.Path.__name__, path)

    @Validator.validate(type=PolicyModel, required_properties=ModelRequiredProperties.POLICY_MODEL)
    def Policies(self, *policies: PolicyModel):
        return self._set_property(self.Policies.__name__, [pm.__to_dict__() for pm in list(policies)])

