from pyformation.resources.shared import BaseCloudFormationResourceModel, Tag


class User(BaseCloudFormationResourceModel):
    __TYPE = "AWS::IAM::User"
    __PROPERTY_GROUPS = "Groups"
    __PROPERTY_LOGIN_PROFILE = "LoginProfile"
    __PROPERTY_MANAGED_POLICY_ARNS = "ManagedPolicyArns"
    __PROPERTY_PATH = "Path"
    __PROPERTY_PERMISSION_BOUNDARY = "PermissionBoundary"
    __PROPERTY_POLICIES = "Policies"
    __PROPERTY_TAGS = "Tags"
    __PROPERTY_USER_NAME = "UserName"

    class LoginProfile:
        __PROPERTY_PASSWORD = "Password"
        __PROPERTY_PASSWORD_RESET_REQUIRED = "PasswordResetRequired"

        def __init__(self):
            self.__login_profile_def = {}

        def create(self):
            return self.__login_profile_def
        
        def password(self, value: str):
            self.__login_profile_def[self.__PROPERTY_PASSWORD] = value

            return self

        def password_reset_required(self, value: bool):
            self.__login_profile_def[self.__PROPERTY_PASSWORD_RESET_REQUIRED] = value

            return self

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
        super(User, self).__init__(type=self.__TYPE)

    def groups(self, *value: str):
        return self._add_property_field(self.__PROPERTY_GROUPS, list(value))

    def login_profile(self, value: LoginProfile):
        return self._add_property_field(self.__PROPERTY_LOGIN_PROFILE, value.create())

    def managed_policy_arns(self, *value: str):
        return self._add_property_field(self.__PROPERTY_MANAGED_POLICY_ARNS, list(value))

    def path(self, value: str):
        return self._add_property_field(self.__PROPERTY_PATH, value)

    def permission_boundary(self, value: str):
        return self._add_property_field(self.__PROPERTY_PERMISSION_BOUNDARY, value)

    def policies(self, *value: Policy):
        return self._add_property_field(self.__PROPERTY_POLICIES, [policy.create() for policy in list(value)])

    def tags(self, *value: Tag):
        return self._add_property_field(self.__PROPERTY_TAGS, [tag.create() for tag in list(value)])

    def username(self, value: str):
        return self._add_property_field(self.__PROPERTY_USER_NAME, value)
