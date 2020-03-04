from resources.shared.base_cf_resource_model import BaseCloudFormationResourceModel
from resources.shared.tag import Tag
from typing import List


class Role(BaseCloudFormationResourceModel):
    __TYPE = "AWS::IAM:Role"
    __PROPERTY_ASSUME_ROLE_POLICY_DOCUMENT = "AssumeRolePolicyDocument"
    __PROPERTY_DESCRIPTION = "Description"
    __PROPERTY_MANAGED_POLICY_ARNS = "ManagedPolicyArns"
    __PROPERTY_MAX_SESSION_DURATION = "MaxSessionDuration"
    __PROPERTY_PATH = "Path"
    __PROPERTY_PERMISSION_BOUNDARY = "PermissionBoundary"
    __PROPERTY_POLICIES = "Policies"
    __PROPERTY_ROLE_NAME = "RoleName"
    __PROPERTY_TAGS = "Tags"

    class Policy:
        __PROPERTY_POLICY_DOCUMENT = "PolicyDocument"
        __PROPERTY_POLICY_NAME = "PolicyName"

        def __init__(self):
            self.__policy_def = {}

        def create(self):
            return self.__policy_def

        def policy_document(self, value: dict):
            self.__policy_def[self.__PROPERTY_POLICY_NAME] = value

            return self

        def policy_name(self, value: str):
            self.__policy_def[self.__PROPERTY_POLICY_NAME] = value

            return self

    def __init__(self):
        super(Role, self).__init__(type=self.__TYPE)

    def assume_role_policy_document(self, value: dict):
        return self._add_property_field(self.__PROPERTY_ASSUME_ROLE_POLICY_DOCUMENT, value)

    def description(self, value: str):
        return self._add_property_field(self.__PROPERTY_DESCRIPTION, value)

    def managed_policy_arns(self, value: List[str]):
        return self._add_property_field(self.__PROPERTY_MANAGED_POLICY_ARNS, value)

    def max_session_duration(self, value: int):
        return self._add_property_field(self.__PROPERTY_MAX_SESSION_DURATION, value)

    def path(self, value: str):
        return self._add_property_field(self.__PROPERTY_PATH, value)

    def permission_boundary(self, value: str):
        return self._add_property_field(self.__PROPERTY_PERMISSION_BOUNDARY, value)

    def policies(self, value: List[Policy]):
        return self._add_property_field(self.__PROPERTY_POLICIES, [policy.create() for policy in value])

    def role_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_ROLE_NAME, value)

    def tags(self, value: List[Tag]):
        return self._add_property_field(self.__PROPERTY_TAGS, [tag.create() for tag in value])
