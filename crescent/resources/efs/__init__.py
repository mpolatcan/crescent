from .file_system import *
from .mount_target import *
from .arn import AccessPointArn, FileSystemArn


class Efs:
    class Arn:
        @staticmethod
        def AccessPointArn(access_point_id: str,
                           partition: str = "aws",
                           region: str = "",
                           account_id: str = ""):
            return AccessPointArn(
                access_point_id=access_point_id,
                partition=partition,
                region=region,
                account_id=account_id
            )

        @staticmethod
        def FileSystemArn(file_system_id: str,
                          partition: str = "aws",
                          region: str = "",
                          account_id: str = ""):
            return FileSystemArn(
                file_system_id=file_system_id,
                partition=partition,
                region=region,
                account_id=account_id
            )

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
    "Efs",
    "AccessPointArn",
    "FileSystemArn"
]