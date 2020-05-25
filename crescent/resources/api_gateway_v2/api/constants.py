from crescent.core.constants import get_values


class BasePath:
    IGNORE = "ignore"
    PREPEND = "prepend"
    SPLIT = "split"


class AllowedValues:
    BASE_PATH = get_values(BasePath)
