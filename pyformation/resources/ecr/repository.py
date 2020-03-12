from pyformation import PyformationResource, Tag
from .lifecycle_policy import LifecyclePolicy


class Repository(PyformationResource):
    __TYPE = "AWS::ECR::Repository"

    def __init__(self, id: str):
        super(Repository, self).__init__(id, self.__TYPE)

    def LifecyclePolicy(self, value: LifecyclePolicy):
        return self._set_property(self.LifecyclePolicy.__name__, value.__to_dict__())

    def RepositoryName(self, value: str):
        return self._set_property(self.RepositoryName.__name__, value)

    def RepositoryPolicyText(self, value: dict):
        return self._set_property(self.RepositoryPolicyText.__name__, value)

    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))
