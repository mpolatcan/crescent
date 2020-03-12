from .file_system import FileSystem, LifecyclePolicy, ElasticFileSystemTag
from .mount_target import MountTarget


class EfsFactory:
    @staticmethod
    def FileSystem(id):
        return FileSystem(id)

    @staticmethod
    def LifecyclePolicy():
        return LifecyclePolicy()

    @staticmethod
    def EfsTag(key, value):
        return ElasticFileSystemTag(key, value)

    @staticmethod
    def MountTarget():
        return MountTarget()


__all__ = [
    "EfsFactory",
    "FileSystem",
    "LifecyclePolicy",
    "ElasticFileSystemTag",
    "MountTarget"
]
