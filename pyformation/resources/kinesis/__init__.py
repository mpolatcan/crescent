from .stream import Stream, StreamEncryption
from .stream_consumer import StreamConsumer


class KinesisFactory:
    @staticmethod
    def Stream(id: str):
        return Stream(id)

    @staticmethod
    def StreamEncryption():
        return StreamEncryption()

    @staticmethod
    def StreamConsumer(id: str):
        return StreamConsumer(id)


__all__ = [
    "KinesisFactory"
]