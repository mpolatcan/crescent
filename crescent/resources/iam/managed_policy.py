from crescent.core import Resource, Validator


class ManagedPolicy(Resource):
    __TYPE = "AWS::IAM::ManagedPolicy"

    def __init__(self, id: str):
        super(ManagedPolicy, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str, max_length=1000)
    def Description(self, description: str):
        return self._set_property(self.Description.__name__, description)

    @Validator.validate(type=str, min_length=1, max_length=128, pattern=r"[\w+=,.@-]+")
    def Groups(self, *groups: str):
        return self._set_property(self.Groups.__name__, list(groups))

    @Validator.validate(type=str)
    def ManagedPolicyName(self, managed_policy_name: str):
        return self._set_property(self.ManagedPolicyName.__name__, managed_policy_name)

    @Validator.validate(type=str, min_length=1, max_length=512, pattern=r"((/[A-Za-z0-9\.,\+@=_-]+)*)/")
    def Path(self, path: str):
        return self._set_property(self.Path.__name__, path)

    @Validator.validate(type=dict, min_length=1, max_length=131072, pattern=r"[\u0009\u000A\u000D\u0020-\u00FF]+")
    def PolicyDocument(self, policy_document: dict):
        return self._set_property(self.PolicyDocument.__name__, policy_document)

    @Validator.validate(type=str)
    def Roles(self, *roles: str):
        return self._set_property(self.Roles.__name__, list(roles))

    @Validator.validate(type=str, min_length=1, max_length=64, pattern=r"[\w+=,.@-]+")
    def Users(self, *users: str):
        return self._set_property(self.Users.__name__, list(users))
