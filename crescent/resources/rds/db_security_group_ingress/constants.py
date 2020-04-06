from crescent.core.constants import get_values


class _RequiredProperties:
    class DBSecurityGroupIngress:
        DB_SECURITY_GROUP_NAME = "DBSecurityGroupName"


# -----------------------------------


class ResourceRequiredProperties:
    DB_SECURITY_GROUP_INGRESS = get_values(_RequiredProperties.DBSecurityGroupIngress)
