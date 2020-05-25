from .efs_tag import ElasticFileSystemTag
from .file_system import FileSystem
from .lifecycle_policy import LifecyclePolicy
from .constants import TransitionToIA, PerformanceMode, ThroughtputMode


class FileSystemFactory:
    ThroughtputMode = ThroughtputMode
    PerformanceMode = PerformanceMode
    TransitionToIA = TransitionToIA

    @staticmethod
    def Create(id: str): return FileSystem(id)

    @staticmethod
    def LifecyclePolicy(): return LifecyclePolicy()

    @staticmethod
    def EfsTag(key: str, value: str): return ElasticFileSystemTag(key, value)


__all__ = ["FileSystemFactory"]
