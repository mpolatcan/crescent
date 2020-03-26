# TODO Event types will be added
class RdsEvent(str):
    def __new__(cls, code):
        return super(RdsEvent, cls).__new__(cls, "RDS-EVENT-{}".format(code))


class RdsEvents:
    class DBInstance:
        class Availability:
            RDS_EVENT_0006 = RdsEvent("0006")
            RDS_EVENT_0004 = RdsEvent("0004")
            RDS_EVENT_0022 = RdsEvent("0022")

        class Backup:
            RDS_EVENT_0001 = RdsEvent("0001")
            RDS_EVENT_0002 = RdsEvent("0002")

        class ConfigurationChange:
            RDS_EVENT_0009 = RdsEvent("0009")
            RDS_EVENT_0024 = RdsEvent("0024")
            RDS_EVENT_0030 = RdsEvent("0030")
            RDS_EVENT_0012 = RdsEvent("0012")
            RDS_EVENT_0018 = RdsEvent("0018")
            RDS_EVENT_0011 = RdsEvent("0011")
            RDS_EVENT_0092 = RdsEvent("0092")
            RDS_EVENT_0028 = RdsEvent("0028")
            RDS_EVENT_0032 = RdsEvent("0032")
            RDS_EVENT_0033 = RdsEvent("0033")
            RDS_EVENT_0025 = RdsEvent("0025")
            RDS_EVENT_0029 = RdsEvent("0029")
            RDS_EVENT_0014 = RdsEvent("0014")
            RDS_EVENT_0017 = RdsEvent("0017")
            RDS_EVENT_0010 = RdsEvent("0010")
            RDS_EVENT_0016 = RdsEvent("0016")
            RDS_EVENT_0067 = RdsEvent("0067")
            RDS_EVENT_0078 = RdsEvent("0078")

        class Creation:
            RDS_EVENT_0005 = RdsEvent("0005")

        class Deletion:
            RDS_EVENT_0003 = RdsEvent("0003")

        class Failover:
            RDS_EVENT_0034 = RdsEvent("0034")
            RDS_EVENT_0013 = RdsEvent("0013")
            RDS_EVENT_0015 = RdsEvent("0015")
            RDS_EVENT_0065 = RdsEvent("0065")
            RDS_EVENT_0049 = RdsEvent("0049")
            RDS_EVENT_0050 = RdsEvent("0050")
            RDS_EVENT_0051 = RdsEvent("0051")

        class Failure:
            RDS_EVENT_0031 = RdsEvent("0031")
            RDS_EVENT_0036 = RdsEvent("0036")
            RDS_EVENT_0035 = RdsEvent("0035")
            RDS_EVENT_0058 = RdsEvent("0058")
            RDS_EVENT_0079 = RdsEvent("0079")
            RDS_EVENT_0080 = RdsEvent("0080")
            RDS_EVENT_0081 = RdsEvent("0081")

        class LowStorage:
            RDS_EVENT_0089 = RdsEvent("0089")
            RDS_EVENT_0007 = RdsEvent("0007")

        class Maintenance:
            RDS_EVENT_0026 = RdsEvent("0026")
            RDS_EVENT_0027 = RdsEvent("0027")
            RDS_EVENT_0047 = RdsEvent("0047")
            RDS_EVENT_0155 = RdsEvent("0155")

        class Notification:
            RDS_EVENT_0044 = RdsEvent("0044")
            RDS_EVENT_0048 = RdsEvent("0048")
            RDS_EVENT_0054 = RdsEvent("0054")
            RDS_EVENT_0055 = RdsEvent("0055")
            RDS_EVENT_0056 = RdsEvent("0056")
            RDS_EVENT_0064 = RdsEvent("0064")
            RDS_EVENT_0084 = RdsEvent("0084")
            RDS_EVENT_0087 = RdsEvent("0087")
            RDS_EVENT_0088 = RdsEvent("0088")
            RDS_EVENT_0154 = RdsEvent("0154")
            RDS_EVENT_0157 = RdsEvent("0157")
            RDS_EVENT_0158 = RdsEvent("0158")

        class ReadReplica:
            RDS_EVENT_0045 = RdsEvent("0045")
            RDS_EVENT_0046 = RdsEvent("0046")
            RDS_EVENT_0057 = RdsEvent("0057")
            RDS_EVENT_0062 = RdsEvent("0062")
            RDS_EVENT_0063 = RdsEvent("0063")

        class Recovery:
            RDS_EVENT_0020 = RdsEvent("0020")
            RDS_EVENT_0021 = RdsEvent("0021")
            RDS_EVENT_0023 = RdsEvent("0023")
            RDS_EVENT_0052 = RdsEvent("0052")
            RDS_EVENT_0053 = RdsEvent("0053")
            RDS_EVENT_0066 = RdsEvent("0066")

        class Restoration:
            RDS_EVENT_0008 = RdsEvent("0008")
            RDS_EVENT_0019 = RdsEvent("0019")

    class DBParameterGroup:
        class ConfigurationChange:
            RDS_EVENT_0037 = RdsEvent("0037")

    class DBSecurityGroup:
        class ConfigurationChange:
            RDS_EVENT_0038 = RdsEvent("0038")

        class Failure:
            RDS_EVENT_0039 = RdsEvent("0039")

    class DBSnapshot:
        class Creation:
            RDS_EVENT_0040 = RdsEvent("0040")
            RDS_EVENT_0042 = RdsEvent("0042")
            RDS_EVENT_0090 = RdsEvent("0090")
            RDS_EVENT_0091 = RdsEvent("0091")
# -----------------------------------------------------------


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
