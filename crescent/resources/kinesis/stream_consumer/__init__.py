from .stream_consumer import StreamConsumer


class StreamConsumerFactory:
    @staticmethod
    def Create(id: str): return StreamConsumer(id)


__all__ = ["StreamConsumerFactory"]
