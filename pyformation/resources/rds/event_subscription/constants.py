class SourceType:
    DB_INSTANCE = "db-instance"
    DB_PARAMETER_GROUP = "db-parameter-group"
    DB_SECURITY_GROUP = "db-security-group"
    DB_SNAPSHOT = "db-snapshot"

# -----------------------------------------------------------


class Property:
    EVENT_SUBSCRIPTION_SOURCE_TYPE = "SourceType"

# -----------------------------------------------------------


class Conditions:
    EVENT_SUBSCRIPTION_SOURCE_IDS = [
        (
            [Property.EVENT_SUBSCRIPTION_SOURCE_TYPE],
            None
        )
    ]

# -----------------------------------------------------------


class AllowedValues:
    SOURCE_TYPE = [
        SourceType.DB_INSTANCE,
        SourceType.DB_PARAMETER_GROUP,
        SourceType.DB_SECURITY_GROUP,
        SourceType.DB_SNAPSHOT
    ]
