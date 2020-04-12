from crescent.core import Resource
from crescent.functions import AnyFn
from .constants import ResourceRequiredProperties
from typing import Union


class Policy(Resource):
    __TYPE = "AWS::IAM::Policy"

    def __init__(self, id: str):
        super(Policy, self).__init__(
            id=id,
            type=self.__TYPE,
            min_length={self.Groups.__name__: 1,
                        self.PolicyDocument.__name__: 1,
                        self.PolicyName.__name__: 1,
                        self.Users.__name__: 1},
            max_length={self.Groups.__name__: 128,
                        self.PolicyDocument.__name__: 131072,
                        self.PolicyName.__name__: 128,
                        self.Users.__name__: 128},
            pattern={self.Groups.__name__: r"[\w+=,.@-]+",
                     self.PolicyDocument.__name__: r"[\u0009\u000A\u000D\u0020-\u00FF]+",
                     self.PolicyName.__name__: r"[\w+=,.@-]+",
                     self.Users.__name__: r"[\w+=,.@-]+"},
            required_properties=ResourceRequiredProperties.POLICY
        )

    def Groups(self, *groups: Union[str, AnyFn]):
        return self._set_property(self.Groups.__name__, list(groups))

    def PolicyDocument(self, policy_document: Union[dict, AnyFn]):
        return self._set_property(self.PolicyDocument.__name__, policy_document)

    def PolicyName(self, policy_name: Union[str, AnyFn]):
        return self._set_property(self.PolicyName.__name__, policy_name)

    def Roles(self, *roles: Union[str, AnyFn]):
        return self._set_property(self.Roles.__name__, list(roles))

    def Users(self, *users: Union[str, AnyFn]):
        return self._set_property(self.Users.__name__, list(users))
