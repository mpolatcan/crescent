from crescent.resources.efs import AccessPointArn, FileSystemArn
from .action import Action, AccessLevelAllActions
from typing import Union


class EfsAction(Action):
    __SERVICE_EFS = "efs"

    def __init__(self, action_name, **definable_resources):
        super(EfsAction, self).__init__(self.__SERVICE_EFS, action_name, **definable_resources)

    def FileSystem(self, value: Union[str, FileSystemArn]):
        return self._set_resource(self.FileSystem.__name__, value)

    def AccessPoint(self, value: Union[str, AccessPointArn]):
        return self._set_resource(self.AccessPoint.__name__, value)

# ---------------------------------------------


class EfsAccessLevelAllActions(AccessLevelAllActions):
    def __init__(self, access_level):
        super(EfsAccessLevelAllActions, self).__init__(access_level)

    def FileSystem(self, file_system: Union[str, FileSystemArn]):
        return self._set_all_actions_resources(self.FileSystem.__name__, file_system)

    def AccessPoint(self, access_point: Union[str, AccessPointArn]):
        return self._set_all_actions_resources(self.AccessPoint.__name__, access_point)


# ---------------------------------------------


class Actions:
    class Write:
        @staticmethod
        def Backup(): return EfsAction(Actions.Write.Backup.__name__, required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def ClientRootAccess(): return EfsAction(Actions.Write.ClientRootAccess.__name__,
                                                 required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def ClientWrite(): return EfsAction(Actions.Write.ClientWrite.__name__,
                                            required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def CreateAccessPoint(): return EfsAction(Actions.Write.CreateAccessPoint.__name__,
                                                  required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def CreateMountTarget(): return EfsAction(Actions.Write.CreateMountTarget.__name__,
                                                  required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def DeleteAccessPoint(): return EfsAction(Actions.Write.DeleteAccessPoint.__name__,
                                                  required=[EfsAction.AccessPoint.__name__])

        @staticmethod
        def DeleteFileSystem(): return EfsAction(Actions.Write.DeleteFileSystem.__name__,
                                                 required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def DeleteFileSystemPolicy(): return EfsAction(Actions.Write.DeleteFileSystemPolicy.__name__,
                                                       required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def DeleteMountTarget(): return EfsAction(Actions.Write.DeleteMountTarget.__name__,
                                                  required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def ModifyMountTargetSecurityGroups(): return EfsAction(Actions.Write.ModifyMountTargetSecurityGroups.__name__,
                                                                required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def PutFileSystemPolicy(): return EfsAction(Actions.Write.PutFileSystemPolicy.__name__,
                                                    required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def PutLifecycleConfiguration(): return EfsAction(Actions.Write.PutLifecycleConfiguration.__name__,
                                                          required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def Restore(): return EfsAction(Actions.Write.Restore.__name__, required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def UpdateFileSystem(): return EfsAction(Actions.Write.UpdateFileSystem.__name__,
                                                 required=[EfsAction.FileSystem.__name__])

    class Read:
        @staticmethod
        def ClientMount(): return EfsAction(Actions.Read.ClientMount.__name__)

        @staticmethod
        def DescribeFileSystemPolicy(): return EfsAction(Actions.Read.DescribeFileSystemPolicy.__name__,
                                                         required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def DescribeLifecycleConfiguration(): return EfsAction(Actions.Read.DescribeLifecycleConfiguration.__name__,
                                                               required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def DescribeMountTargetSecurityGroups(): return EfsAction(Actions.Read.DescribeMountTargetSecurityGroups.__name__,
                                                                  required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def DescribeMountTargets(): return EfsAction(Actions.Read.DescribeMountTargets.__name__,
                                                     required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def DescribeTags(): return EfsAction(Actions.Read.DescribeTags.__name__,
                                             required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def ListTagsForResource(): return EfsAction(Actions.Read.ListTagsForResource.__name__,
                                                    required=[EfsAction.FileSystem.__name__])

    class List:
        @staticmethod
        def DescribeAccessPoints(): return EfsAction(Actions.List.DescribeAccessPoints.__name__,
                                                     required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def DescribeFileSystem(): return EfsAction(Actions.List.DescribeFileSystem.__name__,
                                                   required=[EfsAction.FileSystem.__name__])

    class Tagging:
        @staticmethod
        def CreateFileSystem(): return EfsAction(Actions.Tagging.CreateFileSystem.__name__)

        @staticmethod
        def CreateTags(): return EfsAction(Actions.Tagging.CreateTags.__name__,
                                           required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def DeleteTags(): return EfsAction(Actions.Tagging.DeleteTags.__name__,
                                           required=[EfsAction.FileSystem.__name__])

        @staticmethod
        def TagResource(): return EfsAction(Actions.Tagging.TagResource.__name__)

        @staticmethod
        def UntagResource(): return EfsAction(Actions.Tagging.UntagResource.__name__)

    @staticmethod
    def WriteAll(): return EfsAccessLevelAllActions(Actions.Write)

    @staticmethod
    def ReadAll(): return EfsAccessLevelAllActions(Actions.Read)

    @staticmethod
    def ListAll(): return EfsAccessLevelAllActions(Actions.List)

    @staticmethod
    def TaggingAll(): return EfsAccessLevelAllActions(Actions.Tagging)

    All = "efs:*"
