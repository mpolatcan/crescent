class AccessKeyStatus:
    ACTIVE = "Active"
    INACTIVE = "Inactive"

# -----------------------------------------------------------


class Property:
    POLICY_MODEL_POLICY_DOCUMENT = "PolicyDocument"
    POLICY_MODEL_POLICY_NAME = "PolicyName"
    LOGIN_PROFILE_PASSWORD = "Password"

# -----------------------------------------------------------


class RequiredProperties:
    POLICY_MODEL = [
        Property.POLICY_MODEL_POLICY_DOCUMENT,
        Property.POLICY_MODEL_POLICY_NAME
    ]
    LOGIN_PROFILE = [
        Property.LOGIN_PROFILE_PASSWORD
    ]

# -----------------------------------------------------------


class AllowedValues:
    STATUS = [
        AccessKeyStatus.ACTIVE,
        AccessKeyStatus.INACTIVE
    ]
