from crescent.core.constants import get_values


class _RequiredProperties:
    class OptionConfiguration:
        OPTION_NAME = "OptionName"

    class OptionGroup:
        ENGINE_NAME = "EngineName"
        MAJOR_ENGINE_VERSION = "MajorEngineVersion"
        OPTION_CONFIGURATIONS = "OptionConfigurations"
        OPTION_GROUP_DESCRIPTION = "OptionGroupDescription"

# -----------------------------------------------------------


class ModelRequiredProperties:
    OPTION_CONFIGURATION = get_values(_RequiredProperties.OptionConfiguration)

# -----------------------------------------------------------


class ResourceRequiredProperties:
    OPTION_GROUP = get_values(_RequiredProperties.OptionGroup)
