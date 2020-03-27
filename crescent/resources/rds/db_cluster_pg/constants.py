from crescent.core.constants import get_values


class Family:
    AURORA_5_6 = "aurora5.6"
    AURORA_MYSQL_5_7 = "aurora-mysql5.7"
    AURORA_POSTGRESQL_9_6 = "aurora-postgresql9.6"


class AllowedValues:
    FAMILY = get_values(Family)
