from crescent.core import Resource, Validator, Tag
from .lifecycle_policy import LifecyclePolicy


class Repository(Resource):
    __TYPE = "AWS::ECR::Repository"

    def __init__(self, id: str):
        super(Repository, self).__init__(id, self.__TYPE)

    @Validator.validate(type=LifecyclePolicy)
    def LifecyclePolicy(self, lifecycle_policy: LifecyclePolicy):
        return self._set_property(self.LifecyclePolicy.__name__, lifecycle_policy.__to_dict__())

    @Validator.validate(type=str, min_length=5, max_length=256, pattern=r"(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*")
    def RepositoryName(self, repository_name: str):
        return self._set_property(self.RepositoryName.__name__, repository_name)

    @Validator.validate(type=dict)
    def RepositoryPolicyText(self, repository_policy_text: dict):
        return self._set_property(self.RepositoryPolicyText.__name__, repository_policy_text)

    @Validator.validate(type=Tag)
    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))
