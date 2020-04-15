from .file_system import *
from .mount_target import *
from .arn import AccessPointArn, FileSystemArn


class Efs:
    class Arn:
        @staticmethod
        def AccessPointArn(access_point_id: str, region: str = "", account_id: str = "", partition: str = "aws"):
            return AccessPointArn(access_point_id=access_point_id, region=region,
                                  account_id=account_id, partition=partition)

        @staticmethod
        def FileSystemArn(file_system_id: str, region: str = "", account_id: str = "", partition: str = "aws"):
            return FileSystemArn(file_system_id=file_system_id, region=region,
                                 account_id=account_id, partition=partition)

    class FileSystem:
        ThroughtputMode = ThroughtputMode
        PerformanceMode = PerformanceMode
        TransitionToIA = TransitionToIA

        @staticmethod
        def Create(id: str): return FileSystem(id)

        @staticmethod
        def LifecyclePolicy(): return LifecyclePolicy()

        @staticmethod
        def EfsTag(key: str, value: str): return ElasticFileSystemTag(key, value)

    class MountTarget:
        @staticmethod
        def Create(id: str): return MountTarget(id)


__all__ = [
    "Efs",
    "AccessPointArn",
    "FileSystemArn"
]