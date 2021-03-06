from crescent.resources.ecr import RepositoryArn
from .action import Action, AccessLevelAllActions
from typing import Union


class EcrAction(Action):
    __SERVICE_ECR = "ecr"

    def __init__(self, action_name, **definable_resources):
        super(EcrAction, self).__init__(self.__SERVICE_ECR, action_name, **definable_resources)

    def Repository(self, repository: Union[str, RepositoryArn]):
        return self._set_resource(self.Repository.__name__, repository)

# ------------------------------------


class EcrAccessLevelAllActions(AccessLevelAllActions):
    def __init__(self, access_level):
        super(EcrAccessLevelAllActions, self).__init__(access_level)

    def Repository(self, repository: Union[str, RepositoryArn]):
        return self._set_all_actions_resources(self.Repository.__name__, repository)

# -------------------------------------


class Actions:
    class Read:
        @staticmethod
        def BatchCheckLayerAvailability(): return EcrAction(Actions.Read.BatchCheckLayerAvailability.__name__,
                                                            required=[EcrAction.Repository.__name__])

        @staticmethod
        def BatchGetImage(): return EcrAction(Actions.Read.BatchGetImage.__name__,
                                              required=[EcrAction.Repository.__name__])

        @staticmethod
        def DescribeImageScanFindings(): return EcrAction(Actions.Read.DescribeImageScanFindings.__name__,
                                                          required=[EcrAction.Repository.__name__])

        @staticmethod
        def DescribeImages(): return EcrAction(Actions.Read.DescribeImages.__name__,
                                               required=[EcrAction.Repository.__name__])

        @staticmethod
        def GetAuthorizationToken(): return EcrAction(Actions.Read.GetAuthorizationToken.__name__,
                                                      required=[EcrAction.Repository.__name__])

        @staticmethod
        def GetDownloadUrlForLayer(): return EcrAction(Actions.Read.GetDownloadUrlForLayer.__name__,
                                                       required=[EcrAction.Repository.__name__])

        @staticmethod
        def GetLifecyclePolicy(): return EcrAction(Actions.Read.GetLifecyclePolicy.__name__,
                                                   required=[EcrAction.Repository.__name__])

        @staticmethod
        def GetLifecyclePolicyPreview(): return EcrAction(Actions.Read.GetLifecyclePolicyPreview.__name__,
                                                          required=[EcrAction.Repository.__name__])

        @staticmethod
        def GetRepositoryPolicy(): return EcrAction(Actions.Read.GetRepositoryPolicy.__name__,
                                                    required=[EcrAction.Repository.__name__])

        @staticmethod
        def ListTagsForResource(): return EcrAction(Actions.Read.ListTagsForResource.__name__,
                                                    required=[EcrAction.Repository.__name__])

    class Write:
        @staticmethod
        def BatchDeleteImage(): return EcrAction(Actions.Write.BatchDeleteImage.__name__,
                                                 required=[EcrAction.Repository.__name__])

        @staticmethod
        def CompleteLayerUpload(): return EcrAction(Actions.Write.CompleteLayerUpload.__name__,
                                                    required=[EcrAction.Repository.__name__])

        @staticmethod
        def CreateRepository(): return EcrAction(Actions.Write.CreateRepository.__name__,
                                                 required=[EcrAction.Repository.__name__])

        @staticmethod
        def DeleteLifecyclePolicy(): return EcrAction(Actions.Write.DeleteLifecyclePolicy.__name__,
                                                      required=[EcrAction.Repository.__name__])

        @staticmethod
        def DeleteRepository(): return EcrAction(Actions.Write.DeleteRepository.__name__,
                                                 required=[EcrAction.Repository.__name__])

        @staticmethod
        def DeleteRepositoryPolicy(): return EcrAction(Actions.Write.DeleteRepositoryPolicy.__name__,
                                                       required=[EcrAction.Repository.__name__])

        @staticmethod
        def InitiateLayerUpload(): return EcrAction(Actions.Write.InitiateLayerUpload.__name__,
                                                    required=[EcrAction.Repository.__name__])

        @staticmethod
        def PutImage(): return EcrAction(Actions.Write.PutImage.__name__, required=[EcrAction.Repository.__name__])

        @staticmethod
        def PutImageScanningConfiguration(): return EcrAction(Actions.Write.PutImageScanningConfiguration.__name__,
                                                              required=[EcrAction.Repository.__name__])

        @staticmethod
        def PutImageTagMutability(): return EcrAction(Actions.Write.PutImageTagMutability.__name__,
                                                      required=[EcrAction.Repository.__name__])

        @staticmethod
        def PutLifecyclePolicy(): return EcrAction(Actions.Write.PutLifecyclePolicy.__name__,
                                                   required=[EcrAction.Repository.__name__])

        @staticmethod
        def StartImageScan(): return EcrAction(Actions.Write.StartImageScan.__name__,
                                               required=[EcrAction.Repository.__name__])

        @staticmethod
        def StartLifecyclePolicyPreview(): return EcrAction(Actions.Write.StartLifecyclePolicyPreview.__name__,
                                                            required=[EcrAction.Repository.__name__])

        @staticmethod
        def UploadLayerPart(): return EcrAction(Actions.Write.UploadLayerPart.__name__,
                                                required=[EcrAction.Repository.__name__])

    class List:
        @staticmethod
        def DescribeRepositories(): return EcrAction(Actions.List.DescribeRepositories.__name__,
                                                     required=[EcrAction.Repository.__name__])

        @staticmethod
        def ListImages(): return EcrAction(Actions.List.ListImages.__name__, required=[EcrAction.Repository.__name__])

    class PermissionsManagement:
        @staticmethod
        def SetRepositoryPolicy(): return EcrAction(Actions.PermissionsManagement.SetRepositoryPolicy.__name__,
                                                    required=[EcrAction.Repository.__name__])

    class Tagging:
        @staticmethod
        def TagResource(): return EcrAction(Actions.Tagging.TagResource.__name__,
                                            required=[EcrAction.Repository.__name__])

        @staticmethod
        def UntagResource(): return EcrAction(Actions.Tagging.UntagResource.__name__,
                                              required=[EcrAction.Repository.__name__])

    @staticmethod
    def ReadAll(): return EcrAccessLevelAllActions(Actions.Read)

    @staticmethod
    def WriteAll(): return EcrAccessLevelAllActions(Actions.Write)

    @staticmethod
    def ListAll(): return EcrAccessLevelAllActions(Actions.List)

    @staticmethod
    def TaggingAll(): return EcrAccessLevelAllActions(Actions.Tagging)

    @staticmethod
    def PermissionManagementAll(): return EcrAccessLevelAllActions(Actions.PermissionsManagement)

    All = "ecr:*"
