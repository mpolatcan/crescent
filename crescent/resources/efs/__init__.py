from .file_system import FileSystemFactory
from .mount_target import MountTargetFactory
from .arn import *


class Efs:
    Arn = ArnFactory
    FileSystem = FileSystemFactory
    MountTarget = MountTargetFactory


__all__ = ["Efs", "AccessPointArn", "FileSystemArn"]
