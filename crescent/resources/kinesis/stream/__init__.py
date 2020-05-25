from .stream import Stream
from .stream_encryption import StreamEncryption


class StreamFactory:
    @staticmethod
    def Create(id: str): return Stream(id)

    @staticmethod
    def StreamEncryption(): return StreamEncryption()


__all__ = ["StreamFactory"]