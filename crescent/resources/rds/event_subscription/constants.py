from crescent.core.constants import get_values


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


class _Property:
    class EventSubscription:
        EVENT_CATEGORIES = "EventCategories"
        SOURCE_TYPE = "SourceType"


# -----------------------------------------------------------


class AllowedValues:
    SOURCE_TYPE = get_values(SourceType)

# -----------------------------------------------------------


class Constants:
    EVENT_CATEGORIES = {
        SourceType.DB_INSTANCE: get_values(EventCategories.DBInstance),
        SourceType.DB_PARAMETER_GROUP: get_values(EventCategories.DBParameterGroup),
        SourceType.DB_SECURITY_GROUP: get_values(EventCategories.DBSecurityGroup),
        SourceType.DB_SNAPSHOT: get_values(EventCategories.DBSnapshot),
        SourceType.DB_CLUSTER: get_values(EventCategories.DBCluster),
        SourceType.DB_CLUSTER_SNAPSHOT: get_values(EventCategories.DBClusterSnapshot)
    }

# -----------------------------------------------------------


class Conditions:
    SOURCE_IDS = [
        (
            [_Property.EventSubscription.SOURCE_TYPE],
            lambda source_type: True if source_type is not None else Exception("Property \"SourceType\" must be defined!")
        )
    ]
    EVENT_CATEGORIES = [
        (
            [_Property.EventSubscription.SOURCE_TYPE],
            lambda source_type: Exception("Property \"SourceType\" must be defined!") if source_type is None else True
        ),
        (
            [_Property.EventSubscription.SOURCE_TYPE, _Property.EventSubscription.EVENT_CATEGORIES],
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
