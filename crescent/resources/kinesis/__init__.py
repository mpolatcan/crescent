from .arn import *
from .stream import StreamFactory
from .stream_consumer import StreamConsumerFactory


class Kinesis:
    Arn = ArnFactory
    Stream = StreamFactory
    StreamConsumer = StreamConsumerFactory


__all__ = ["Kinesis", "StreamArn", "StreamConsumerArn"]
