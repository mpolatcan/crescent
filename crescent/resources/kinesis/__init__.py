from .stream import *
from .stream_consumer import *


class Kinesis:
    class Stream:
        @staticmethod
        def Stream(id: str):
            return Stream(id)

        @staticmethod
        def StreamEncryption():
            return StreamEncryption()

    class StreamConsumer:
        @staticmethod
        def StreamConsumer(id: str):
            return StreamConsumer(id)


__all__ = [
    "Kinesis"
]