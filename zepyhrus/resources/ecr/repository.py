from zepyhrus.core import Resource, Validator, Tag
from .lifecycle_policy import LifecyclePolicy


class Repository(Resource):
    __TYPE = "AWS::ECR::Repository"

    def __init__(self, id: str):
        super(Repository, self).__init__(id, self.__TYPE)

    @Validator.validate(type=LifecyclePolicy)
    def LifecyclePolicy(self, value: LifecyclePolicy):
        return self._set_property(self.LifecyclePolicy.__name__, value.__to_dict__())

    @Validator.validate(type=str, min_length=5, max_length=256, pattern=r"(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*")
    def RepositoryName(self, value: str):
        return self._set_property(self.RepositoryName.__name__, value)

    @Validator.validate(type=dict)
    def RepositoryPolicyText(self, value: dict):
        return self._set_property(self.RepositoryPolicyText.__name__, value)

    @Validator.validate(type=Tag)
    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))
