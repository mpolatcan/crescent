from crescent.core.constants import get_values


class _RequiredProperties:
    class AccessPoint:
        BUCKET = "Bucket"


# ----------------------------------------------------


class ResourceRequiredProperties:
    ACCESS_POINT = get_values(_RequiredProperties.AccessPoint)