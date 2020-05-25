from crescent.core.constants import get_values


class _RequiredProperties:
    class VpcLink:
        NAME = "Name"
        SUBNET_IDS = "SubnetIds"


class ResourceRequiredProperties:
    VPC_LINK = get_values(_RequiredProperties.VpcLink)
