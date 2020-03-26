from .file_system import *
from .mount_target import *


class Efs:
    class FileSystem:
        ThroughtputMode = ThroughtputMode
        PerformanceMode = PerformanceMode
        TransitionToIA = TransitionToIA

        @staticmethod
        def Create(id: str):
            return FileSystem(id)

        @staticmethod
        def LifecyclePolicy():
            return LifecyclePolicy()

        @staticmethod
        def EfsTag(key: str, value: str):
            return ElasticFileSystemTag(key, value)

    class MountTarget:
        @staticmethod
        def Create(id: str):
            return MountTarget(id)


__all__ = [
    "Efs"
]