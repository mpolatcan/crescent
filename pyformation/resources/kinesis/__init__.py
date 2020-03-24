from .stream import Stream, StreamEncryption
from .stream_consumer import StreamConsumer


class KinesisFactory:
    class __KinesisStreamFactory:
        @staticmethod
        def Stream(id: str):
            return Stream(id)

        @staticmethod
        def StreamEncryption():
            return StreamEncryption()

    class __KinesisStreamConsumerFactory:
        @staticmethod
        def StreamConsumer(id: str):
            return StreamConsumer(id)

    stream = __KinesisStreamFactory
    stream_consumer = __KinesisStreamConsumerFactory


kinesis = KinesisFactory
kinesis_stream = kinesis.stream
kinesis_stream_consumer = kinesis.stream_consumer


__all__ = [
    "kinesis",
    "kinesis_stream",
    "kinesis_stream_consumer"
]