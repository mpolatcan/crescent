from crescent.core.constants import get_values


class LoggingLevel:
    INFO = "INFO"
    ERROR = "ERROR"
    OFF = "OFF"


class AllowedValues:
    LOGGING_LEVEL = get_values(LoggingLevel)
