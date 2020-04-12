from crescent.core import Resource
from crescent.functions import AnyFn
from .constants import ResourceRequiredProperties
from typing import Union


class ManagedPolicy(Resource):
    __TYPE = "AWS::IAM::ManagedPolicy"

    def __init__(self, id: str):
        super(ManagedPolicy, self).__init__(
            id=id,
            type=self.__TYPE,
            min_length={self.Groups.__name__: 1,
                        self.Path.__name__: 1,
                        self.PolicyDocument.__name__: 1,
                        self.Users.__name__: 1},
            max_length={self.Description.__name__: 1000,
                        self.Groups.__name__: 128,
                        self.Path.__name__: 512,
                        self.PolicyDocument.__name__: 131072,
                        self.Users.__name__: 64},
            pattern={self.Groups.__name__: r"[\w+=,.@-]+",
                     self.Path.__name__: r"((/[A-Za-z0-9\.,\+@=_-]+)*)/",
                     self.PolicyDocument.__name__: r"[\u0009\u000A\u000D\u0020-\u00FF]+",
                     self.Users.__name__: r"[\w+=,.@-]+"},
            required_properties=ResourceRequiredProperties.MANAGED_POLICY
        )

    def Description(self, description: Union[str, AnyFn]):
        return self._set_property(self.Description.__name__, description)

    def Groups(self, *groups: Union[str, AnyFn]):
        return self._set_property(self.Groups.__name__, list(groups))

    def ManagedPolicyName(self, managed_policy_name: Union[str, AnyFn]):
        return self._set_property(self.ManagedPolicyName.__name__, managed_policy_name)

    def Path(self, path: Union[str, AnyFn]):
        return self._set_property(self.Path.__name__, path)

    def PolicyDocument(self, policy_document: Union[dict, AnyFn]):
        return self._set_property(self.PolicyDocument.__name__, policy_document)

    def Roles(self, *roles: Union[str, AnyFn]):
        return self._set_property(self.Roles.__name__, list(roles))

    def Users(self, *users: Union[str, AnyFn]):
        return self._set_property(self.Users.__name__, list(users))
