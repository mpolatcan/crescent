class EventCategories:
    class DBInstance:
        AVAILABILITY = "availability"
        BACKUP = "backup"
        CONFIGURATION_CHANGE = "configuration change"
        CREATION = "creation"
        DELETION = "deletion"
        FAILOVER = "failover"
        FAILURE = "failure"
        LOW_STORAGE = "low storage"
        MAINTENANCE = "maintenance"
        NOTIFICATION = "notification"
        READ_REPLICA = "read replica"
        RECOVERY = "recovery"
        RESTORATION = "restoration"

    class DBParameterGroup:
        CONFIGURATION_CHANGE = "configuration change"

    class DBSecurityGroup:
        CONFIGURATION_CHANGE = "configuration change"
        FAILURE = "failure"

    class DBSnapshot:
        CREATION = "creation"
        DELETION = "deletion"
        NOTIFICATION = "notification"
        RESTORATION = "restoration"

    class DBCluster:
        FAILOVER = "failover"
        FAILURE = "failure"
        MAINTENANCE = "maintenance"
        NOTIFICATION = "notification"

    class DBClusterSnapshot:
        BACKUP = "backup"
        NOTIFICATION = "notification"
# -----------------------------------------------------------


class SourceType:
    DB_INSTANCE = "db-instance"
    DB_CLUSTER = "db-cluster"
    DB_PARAMETER_GROUP = "db-parameter-group"
    DB_SECURITY_GROUP = "db-security-group"
    DB_SNAPSHOT = "db-snapshot"
    DB_CLUSTER_SNAPSHOT = "db-cluster-snapshot"

# -----------------------------------------------------------


class Property:
    EVENT_SUBSCRIPTION_EVENT_CATEGORIES = "EventCategories"
    EVENT_SUBSCRIPTION_SOURCE_TYPE = "SourceType"


# -----------------------------------------------------------


class AllowedValues:
    SOURCE_TYPE = [
        SourceType.DB_INSTANCE,
        SourceType.DB_CLUSTER,
        SourceType.DB_PARAMETER_GROUP,
        SourceType.DB_SECURITY_GROUP,
        SourceType.DB_SNAPSHOT,
        SourceType.DB_CLUSTER_SNAPSHOT
    ]

# -----------------------------------------------------------


class Constants:
    EVENT_CATEGORIES = {
        SourceType.DB_INSTANCE: [
            EventCategories.DBInstance.AVAILABILITY,
            EventCategories.DBInstance.BACKUP,
            EventCategories.DBInstance.CONFIGURATION_CHANGE,
            EventCategories.DBInstance.CREATION,
            EventCategories.DBInstance.DELETION,
            EventCategories.DBInstance.FAILOVER,
            EventCategories.DBInstance.FAILURE,
            EventCategories.DBInstance.LOW_STORAGE,
            EventCategories.DBInstance.MAINTENANCE,
            EventCategories.DBInstance.NOTIFICATION,
            EventCategories.DBInstance.READ_REPLICA,
            EventCategories.DBInstance.RECOVERY,
            EventCategories.DBInstance.RESTORATION
        ],
        SourceType.DB_PARAMETER_GROUP: [
            EventCategories.DBParameterGroup.CONFIGURATION_CHANGE
        ],
        SourceType.DB_SECURITY_GROUP: [
            EventCategories.DBSecurityGroup.CONFIGURATION_CHANGE,
            EventCategories.DBSecurityGroup.FAILURE
        ],
        SourceType.DB_SNAPSHOT: [
            EventCategories.DBSnapshot.DELETION,
            EventCategories.DBSnapshot.CREATION,
            EventCategories.DBSnapshot.NOTIFICATION,
            EventCategories.DBSnapshot.RESTORATION
        ],
        SourceType.DB_CLUSTER: [
            EventCategories.DBCluster.NOTIFICATION,
            EventCategories.DBCluster.FAILURE,
            EventCategories.DBCluster.FAILOVER,
            EventCategories.DBCluster.MAINTENANCE
        ],
        SourceType.DB_CLUSTER_SNAPSHOT: [
            EventCategories.DBClusterSnapshot.NOTIFICATION,
            EventCategories.DBClusterSnapshot.BACKUP
        ]
    }

# -----------------------------------------------------------


class Conditions:
    SOURCE_IDS = [
        (
            [Property.EVENT_SUBSCRIPTION_SOURCE_TYPE],
            lambda source_type:
                True if source_type is not None
                else Exception("Property SourceType must be provided!")
        )
    ]
    EVENT_CATEGORIES = [
        (
            [Property.EVENT_SUBSCRIPTION_SOURCE_TYPE],
            lambda source_type: Exception("Property \"SourceType\" must be defined!") if source_type is None else True
        ),
        (
            [Property.EVENT_SUBSCRIPTION_SOURCE_TYPE, Property.EVENT_SUBSCRIPTION_EVENT_CATEGORIES],
            lambda source_type, event_categories:
                Exception("Invalid event category \"{category}\" for source type {source_type}".format(
                    category=[
                        event_category for event_category in event_categories
                        if event_category not in Constants.EVENT_CATEGORIES[source_type]
                    ][0],
                    source_type=source_type)
                ) if len([
                    event_category for event_category in event_categories
                    if event_category not in Constants.EVENT_CATEGORIES[source_type]
                ]) > 0 else True
        )
    ]
