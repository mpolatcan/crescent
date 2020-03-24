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


class Property:
    LIFECYCLE_POLICY_TRANSITION_TO_IA = "TransitionToIA"

##########################################


class RequiredProperties:
    LIFECYCLE_POLICY = [
        Property.LIFECYCLE_POLICY_TRANSITION_TO_IA
    ]

##########################################


class AllowedValues:
    PERFORMANCE_MODE = [
        PerformanceMode.GENERAL_PURPOSE,
        PerformanceMode.MAX_IO
    ]
    THROUGHPUT_MODE = [
        ThroughtputMode.BURSTING,
        ThroughtputMode.PROVISIONED
    ]
    TRANSITION_TO_IA = [
        TransitionToIA.AFTER_14_DAYS,
        TransitionToIA.AFTER_30_DAYS,
        TransitionToIA.AFTER_60_DAYS,
        TransitionToIA.AFTER_7_DAYS,
        TransitionToIA.AFTER_90_DAYS
    ]