from crescent.core.constants import get_values


class _RequiredProperties:
    class OptionConfiguration:
        OPTION_NAME = "OptionName"

# -----------------------------------------------------------


class ModelRequiredProperties:
    OPTION_CONFIGURATION = get_values(_RequiredProperties.OptionConfiguration)

