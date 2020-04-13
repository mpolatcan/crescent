from .arn import StreamArn, StreamConsumerArn
from .stream import *
from .stream_consumer import *


class Kinesis:
    class Arn:
        @staticmethod
        def StreamArn(stream_id: str, partition: str = "aws", region: str = "", account_id: str = ""):
            return StreamArn(stream_id=stream_id, partition=partition, region=region, account_id=account_id)

        @staticmethod
        def StreamConsumerArn(stream_type: str, stream_id: str, consumer_id: str, consumer_creation_timpstamps: str = "",
                              partition: str = "aws", region: str = "", account_id: str = ""):
            return StreamConsumerArn(stream_type=stream_type,
                                     stream_id=stream_id,
                                     consumer_id=consumer_id,
                                     consumer_creation_timpstamps=consumer_creation_timpstamps,
                                     partition=partition,
                                     region=region,
                                     account_id=account_id)

    class Stream:
        @staticmethod
        def Create(id: str): return Stream(id)

        @staticmethod
        def StreamEncryption(): return StreamEncryption()

    class StreamConsumer:
        @staticmethod
        def Create(id: str): return StreamConsumer(id)


__all__ = [
    "Kinesis",
    "StreamArn",
    "StreamConsumerArn"
]