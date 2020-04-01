from .action import Action, AccessLevelAllActions
from crescent.core import Validator
from crescent.resources.efs import AccessPointArn, FileSystemArn


class EfsAction(Action):
    __SERVICE_EFS = "efs"

    def __init__(self, action_name, required_resource=None):
        super(EfsAction, self).__init__(self.__SERVICE_EFS, action_name, required_resource)

    @Validator.validate(type=FileSystemArn)
    def FileSystem(self, value: FileSystemArn):
        return self._set_resource(value)

    @Validator.validate(type=AccessPointArn)
    def AccessPoint(self, value: AccessPointArn):
        return self._set_resource(value)

# ---------------------------------------------


class EfsAccessLevelAllActions(AccessLevelAllActions):
    def __init__(self, access_level):
        super(EfsAccessLevelAllActions, self).__init__(access_level)

    def FileSystem(self, file_system: FileSystemArn):
        return [action.FileSystem(file_system) for action in self._actions]

    def AccessPoint(self, access_point: AccessPointArn):
        return [action.AccessPoint(access_point) for action in self._actions]


# ---------------------------------------------


class Actions:
    class Write:
        @staticmethod
        def Backup():
            return EfsAction(Actions.Write.Backup.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def ClientRootAccess():
            return EfsAction(Actions.Write.ClientRootAccess.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def ClientWrite():
            return EfsAction(Actions.Write.ClientWrite.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def CreateAccessPoint():
            return EfsAction(Actions.Write.CreateAccessPoint.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def CreateMountTarget():
            return EfsAction(Actions.Write.CreateMountTarget.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def DeleteAccessPoint():
            return EfsAction(Actions.Write.DeleteAccessPoint.__name__, EfsAction.AccessPoint.__name__)

        @staticmethod
        def DeleteFileSystem():
            return EfsAction(Actions.Write.DeleteFileSystem.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def DeleteFileSystemPolicy():
            return EfsAction(Actions.Write.DeleteFileSystemPolicy.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def DeleteMountTarget():
            return EfsAction(Actions.Write.DeleteMountTarget.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def ModifyMountTargetSecurityGroups():
            return EfsAction(Actions.Write.ModifyMountTargetSecurityGroups.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def PutFileSystemPolicy():
            return EfsAction(Actions.Write.PutFileSystemPolicy.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def PutLifecycleConfiguration():
            return EfsAction(Actions.Write.PutLifecycleConfiguration.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def Restore():
            return EfsAction(Actions.Write.Restore.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def UpdateFileSystem():
            return EfsAction(Actions.Write.UpdateFileSystem.__name__, EfsAction.FileSystem.__name__)

    class Read:
        @staticmethod
        def ClientMount():
            return EfsAction(Actions.Read.ClientMount.__name__)

        @staticmethod
        def DescribeFileSystemPolicy():
            return EfsAction(Actions.Read.DescribeFileSystemPolicy.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def DescribeLifecycleConfiguration():
            return EfsAction(Actions.Read.DescribeLifecycleConfiguration.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def DescribeMountTargetSecurityGroups():
            return EfsAction(Actions.Read.DescribeMountTargetSecurityGroups.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def DescribeMountTargets():
            return EfsAction(Actions.Read.DescribeMountTargets.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def DescribeTags():
            return EfsAction(Actions.Read.DescribeTags.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def ListTagsForResource():
            return EfsAction(Actions.Read.ListTagsForResource.__name__,  EfsAction.FileSystem.__name__)

    class List:
        @staticmethod
        def DescribeAccessPoints():
            return EfsAction(Actions.List.DescribeAccessPoints.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def DescribeFileSystem():
            return EfsAction(Actions.List.DescribeFileSystem.__name__, EfsAction.FileSystem.__name__)

    class Tagging:
        @staticmethod
        def CreateFileSystem():
            return EfsAction(Actions.Tagging.CreateFileSystem.__name__)

        @staticmethod
        def CreateTags():
            return EfsAction(Actions.Tagging.CreateTags.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def DeleteTags():
            return EfsAction(Actions.Tagging.DeleteTags.__name__, EfsAction.FileSystem.__name__)

        @staticmethod
        def TagResource():
            return EfsAction(Actions.Tagging.TagResource.__name__)

        @staticmethod
        def UntagResource():
            return EfsAction(Actions.Tagging.UntagResource.__name__)

    @staticmethod
    def WriteAll():
        return EfsAccessLevelAllActions(Actions.Write)

    @staticmethod
    def ReadAll():
        return EfsAccessLevelAllActions(Actions.Read)

    @staticmethod
    def ListAll():
        return EfsAccessLevelAllActions(Actions.List)

    @staticmethod
    def Tagging():
        return EfsAccessLevelAllActions(Actions.Tagging)

