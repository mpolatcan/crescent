from pyformation.resources.shared import BaseCloudFormationResourceModel, Tag


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

    def managed_policy_arns(self, *value: str):
        return self._add_property_field(self.__PROPERTY_MANAGED_POLICY_ARNS, list(value))

    def max_session_duration(self, value: int):
        return self._add_property_field(self.__PROPERTY_MAX_SESSION_DURATION, value)

    def path(self, value: str):
        return self._add_property_field(self.__PROPERTY_PATH, value)

    def permission_boundary(self, value: str):
        return self._add_property_field(self.__PROPERTY_PERMISSION_BOUNDARY, value)

    def policies(self, *value: Policy):
        return self._add_property_field(self.__PROPERTY_POLICIES, [policy.create() for policy in list(value)])

    def role_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_ROLE_NAME, value)

    def tags(self, *value: Tag):
        return self._add_property_field(self.__PROPERTY_TAGS, [tag.create() for tag in list(value)])
