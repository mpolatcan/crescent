from crescent.core import Resource, Tag
from .lifecycle_policy import LifecyclePolicy


class Repository(Resource):
    __TYPE = "AWS::ECR::Repository"

    def __init__(self, id: str):
        super(Repository, self).__init__(
            id=id,
            type=self.__TYPE,
            min_length={self.RepositoryName.__name__: 5},
            max_length={self.RepositoryName.__name__: 256},
            pattern={self.RepositoryName.__name__: r"(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*"}
        )

    def LifecyclePolicy(self, lifecycle_policy: LifecyclePolicy):
        return self._set_property(self.LifecyclePolicy.__name__, lifecycle_policy)

    def RepositoryName(self, repository_name: str):
        return self._set_property(self.RepositoryName.__name__, repository_name)

    def RepositoryPolicyText(self, repository_policy_text: dict):
        return self._set_property(self.RepositoryPolicyText.__name__, repository_policy_text)

    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))
