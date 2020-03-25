from crescent.core import Resource, Validator
from .policy_model import PolicyModel
from .constants import RequiredProperties


class Group(Resource):
    __TYPE = "AWS::IAM::Group"

    def __init__(self, id: str):
        super(Group, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def GroupName(self, value: str):
        return self._set_property(self.GroupName.__name__, value)

    @Validator.validate(type=str)
    def ManagedPolicyArns(self, *value: str):
        return self._set_property(self.ManagedPolicyArns.__name__, list(value))

    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"(\u002F)|(\u002F[\u0021-\u007F]+\u002F)")
    def Path(self, value: str):
        return self._set_property(self.Path.__name__, value)

    @Validator.validate(type=PolicyModel, required_properties=RequiredProperties.POLICY_MODEL)
    def Policies(self, *value: PolicyModel):
        return self._set_property(self.Policies.__name__, [pm.__to_dict__() for pm in list(value)])

