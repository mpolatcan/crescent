from pyformation.resources.shared import BaseCloudFormationResourceModel, Tag
from pyformation.resources.ecr import LifecyclePolicy


class Repository(BaseCloudFormationResourceModel):
    __TYPE = "AWS::ECR::Repository"
    __PROPERTY_LIFECYCLE_POLICY = "LifecyclePolicy"
    __PROPERTY_REPOSITORY_NAME = "RepositoryName"
    __PROPERTY_REPOSITORY_POLICY_TEXT = "RepositoryPolicyText"
    __PROPERTY_TAGS = "Tags"

    def __init__(self):
        super(Repository, self).__init__(type=self.__TYPE)

    def lifecycle_policy(self, value: LifecyclePolicy):
        return self._add_property_field(self.__PROPERTY_LIFECYCLE_POLICY, value)

    def repository_name(self, value: dict):
        return self._add_property_field(self.__PROPERTY_REPOSITORY_NAME, value)

    def repository_policy_text(self, value: dict):
        return self._add_property_field(self.__PROPERTY_REPOSITORY_POLICY_TEXT, value)

    def tags(self, *value: Tag):
        return self._add_property_field(self.__PROPERTY_TAGS, [
            tag for tag in list(value)
        ])
