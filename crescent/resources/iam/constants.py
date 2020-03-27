from crescent.core.constants import get_values


class AccessKeyStatus:
    ACTIVE = "Active"
    INACTIVE = "Inactive"

# -----------------------------------------------------------


class _RequiredProperties:
    class PolicyModel:
        POLICY_DOCUMENT = "PolicyDocument"
        POLICY_NAME = "PolicyName"

    class LoginProfile:
        PASSWORD = "Password"

# -----------------------------------------------------------


class ModelRequiredProperties:
    POLICY_MODEL = get_values(_RequiredProperties.PolicyModel)
    LOGIN_PROFILE = get_values(_RequiredProperties.LoginProfile)

# -----------------------------------------------------------


class AllowedValues:
    STATUS = get_values(AccessKeyStatus)
