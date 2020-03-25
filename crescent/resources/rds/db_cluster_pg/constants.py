class Family:
    AURORA_5_6 = "aurora5.6"
    AURORA_MYSQL_5_7 = "aurora-mysql5.7"
    AURORA_POSTGRESQL_9_6 = "aurora-postgresql9.6"


class AllowedValues:
    FAMILY = [
        Family.AURORA_5_6,
        Family.AURORA_MYSQL_5_7,
        Family.AURORA_POSTGRESQL_9_6
    ]
