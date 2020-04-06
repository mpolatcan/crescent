from crescent.core.constants import get_values


class _RequiredProperties:
    class DBSecurityGroup:
        DB_SECURITY_GROUP_INGRESS = "DBSecurityGroupIngress"
        GROUP_DESCRIPTION = "GroupDescription"

# ----------------------------------


class ResourceRequiredProperties:
    DB_SECURITY_GROUP = get_values(_RequiredProperties.DBSecurityGroup)