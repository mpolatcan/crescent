from crescent.core.constants import get_values


class _RequiredProperties:
    class DBSubnetGroup:
        DB_SUBNET_GROUP_DESCRIPTION = "DBSubnetGroupDescription"
        SUBNET_IDS = "SubnetIds"

# -------------------------------------


class ResourceRequiredProperties:
    DB_SUBNET_GROUP = get_values(_RequiredProperties.DBSubnetGroup)
