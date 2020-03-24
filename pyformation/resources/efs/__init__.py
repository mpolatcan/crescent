from .file_system import (
    FileSystem,
    LifecyclePolicy,
    ElasticFileSystemTag,
    ThroughtputMode,
    PerformanceMode,
    TransitionToIA
)
from .mount_target import MountTarget


class EfsFactory:
    class __FileSystemFactory:
        throughput_mode = ThroughtputMode
        performance_mode = PerformanceMode
        transition_to_ia = TransitionToIA

        @staticmethod
        def FileSystem(id: str):
            return FileSystem(id)

        @staticmethod
        def LifecyclePolicy():
            return LifecyclePolicy()

        @staticmethod
        def EfsTag(key: str, value: str):
            return ElasticFileSystemTag(key, value)

    class __MountTargetFactory:
        @staticmethod
        def MountTarget(id: str):
            return MountTarget(id)

    file_system = __FileSystemFactory
    mount_target = __MountTargetFactory


efs = EfsFactory
efs_file_system = efs.file_system
efs_mount_target = efs.mount_target


__all__ = [
    "efs",
    "efs_file_system",
    "efs_mount_target"
]
