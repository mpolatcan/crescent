from crescent.core.constants import get_values


class ThroughtputMode:
    BURSTING = "bursting"
    PROVISIONED = "provisioned"

##########################################


class PerformanceMode:
    GENERAL_PURPOSE = "generalPurpose"
    MAX_IO = "maxIO"

##########################################


class TransitionToIA:
    AFTER_14_DAYS = "AFTER_14_DAYS"
    AFTER_30_DAYS = "AFTER_30_DAYS"
    AFTER_60_DAYS = "AFTER_60_DAYS"
    AFTER_7_DAYS = "AFTER_7_DAYS"
    AFTER_90_DAYS = "AFTER_90_DAYS"

##########################################


class _RequiredProperties:
    class LifecyclePolicy:
        TRANSITION_TO_IA = "TransitionToIA"

##########################################


class ModelRequiredProperties:
    LIFECYCLE_POLICY = get_values(_RequiredProperties.LifecyclePolicy)

##########################################


class AllowedValues:
    PERFORMANCE_MODE = get_values(PerformanceMode)
    THROUGHPUT_MODE = get_values(ThroughtputMode)
    TRANSITION_TO_IA = get_values(TransitionToIA)
