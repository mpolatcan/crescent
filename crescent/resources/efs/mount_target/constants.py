from crescent.core.constants import get_values


class _RequiredProperties:
    class MountTarget:
        FILE_SYSTEM_ID = "FileSystemId"
        SECURITY_GROUPS = "SecurityGroups"
        SUBNET_ID = "SubnetId"

# -----------------------------------------


class ResourceRequiredProperties:
    MOUNT_TARGET = get_values(_RequiredProperties.MountTarget)
