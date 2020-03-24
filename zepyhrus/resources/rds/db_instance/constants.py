class Property:
    DB_INSTANCE_ROLE_FEATURE_NAME = "FeatureName"
    DB_INSTANCE_ROLE_ROLE_ARN = "RoleArn"

# -----------------------------------------------------------


class RequiredProperties:
    DB_INSTANCE_ROLE = [
        Property.DB_INSTANCE_ROLE_FEATURE_NAME,
        Property.DB_INSTANCE_ROLE_ROLE_ARN
    ]
