from crescent.core.constants import get_values


class _RequiredProperties:
    class StreamConsumer:
        CONSUMER_NAME = "ConsumerName"
        STREAM_ARN = "StreamARN"

# -----------------------------------------------


class ResourceRequiredProperties:
    STREAM_CONSUMER = get_values(_RequiredProperties.StreamConsumer)