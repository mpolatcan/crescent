from resources.shared import BaseCloudFormationResourceModel


class Group(BaseCloudFormationResourceModel):
    __TYPE = "AWS::IAM::Group"
    __PROPERTY_GROUP_NAME = "GroupName"
    __PROPERTY_MANAGED_POLICY_ARNS = "ManagedPolicyArns"
    __PROPERTY_PATH = "Path"
    __PROPERTY_POLICIES = "Policies"

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
        super(Group, self).__init__(type=self.__TYPE)

    def group_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_GROUP_NAME, value)

    def managed_policy_arns(self, *value: str):
        return self._add_property_field(self.__PROPERTY_MANAGED_POLICY_ARNS, list(value))

    def path(self, value: str):
        return self._add_property_field(self.__PROPERTY_PATH, value)

    def policies(self, *value: Policy):
        return self._add_property_field(self.__PROPERTY_POLICIES, [policy.create() for policy in list(value)])

