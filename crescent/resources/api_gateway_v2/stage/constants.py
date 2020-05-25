from crescent.core.constants import get_values


class _RequiredProperties:
    class Stage:
        API_ID = "ApiId"
        STAGE_NAME = "StageName"


class ResourceRequiredProperties:
    STAGE = get_values(_RequiredProperties.Stage)
