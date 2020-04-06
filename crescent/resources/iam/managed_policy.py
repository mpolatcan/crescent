from crescent.core import Resource
from .constants import ResourceRequiredProperties


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

    def Description(self, description: str):
        return self._set_property(self.Description.__name__, description)

    def Groups(self, *groups: str):
        return self._set_property(self.Groups.__name__, list(groups))

    def ManagedPolicyName(self, managed_policy_name: str):
        return self._set_property(self.ManagedPolicyName.__name__, managed_policy_name)

    def Path(self, path: str):
        return self._set_property(self.Path.__name__, path)

    def PolicyDocument(self, policy_document: dict):
        return self._set_property(self.PolicyDocument.__name__, policy_document)

    def Roles(self, *roles: str):
        return self._set_property(self.Roles.__name__, list(roles))

    def Users(self, *users: str):
        return self._set_property(self.Users.__name__, list(users))
