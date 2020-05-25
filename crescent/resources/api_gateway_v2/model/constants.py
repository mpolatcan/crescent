from crescent.core.constants import get_values


class _RequiredProperties:
    class Model:
        API_ID = "ApiId"
        NAME = "Name"
        SCHEMA = "Schema"


class ResourceRequiredProperties:
    MODEL = get_values(_RequiredProperties.Model)
