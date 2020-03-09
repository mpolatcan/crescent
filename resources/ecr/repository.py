from typing import List
from resources.shared import BaseCloudFormationResourceModel, Tag
from resources.ecr import LifecyclePolicy


class Repository(BaseCloudFormationResourceModel):
    __TYPE = "AWS::ECR::Repository"
    __PROPERTY_LIFECYCLE_POLICY = "LifecyclePolicy"
    __PROPERTY_REPOSITORY_NAME = "RepositoryName"
    __PROPERTY_REPOSITORY_POLICY_TEXT = "RepositoryPolicyText"
    __PROPERTY_TAGS = "Tags"

    def __init__(self):
        super(Repository, self).__init__(type=self.__TYPE)

    def lifecycle_policy(self, value: LifecyclePolicy):
        return self._add_property_field(self.__PROPERTY_LIFECYCLE_POLICY, value.create())

    def repository_name(self, value: dict):
        return self._add_property_field(self.__PROPERTY_REPOSITORY_NAME, value)

    def repository_policy_text(self, value: dict):
        return self._add_property_field(self.__PROPERTY_REPOSITORY_POLICY_TEXT, value)

    def tags(self, value: List[Tag]):
        return self._add_property_field(self.__PROPERTY_TAGS, [
            tag.create() for tag in value
        ])
