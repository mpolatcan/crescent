from .action import Action, AccessLevelAllActions
from crescent.resources.ecr import RepositoryArn
from crescent.core import Validator

__SERVICE_ECR__ = "ecr"


class EcrAction(Action):
    def __init__(self, action_name, required_resource=None):
        super(EcrAction, self).__init__(__SERVICE_ECR__, action_name, required_resource)

    @Validator.validate(type=RepositoryArn)
    def Repository(self, repository: RepositoryArn):
        return self._set_resource(repository)

# ------------------------------------


class EcrAccessLevelAllActions(AccessLevelAllActions):
    def __init__(self, access_level):
        super(EcrAccessLevelAllActions, self).__init__(access_level)

    def Repository(self, repository: RepositoryArn):
        return [action.Repository(repository) for action in self._actions]

# -------------------------------------


class Actions:
    class Read:
        @staticmethod
        def BatchCheckLayerAvailability():
            return EcrAction(Actions.Read.BatchCheckLayerAvailability.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def BatchGetImage():
            return EcrAction(Actions.Read.BatchGetImage.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def DescribeImageScanFindings():
            return EcrAction(Actions.Read.DescribeImageScanFindings.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def DescribeImages():
            return EcrAction(Actions.Read.DescribeImages.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def GetAuthorizationToken():
            return EcrAction(Actions.Read.GetAuthorizationToken.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def GetDownloadUrlForLayer():
            return EcrAction(Actions.Read.GetDownloadUrlForLayer.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def GetLifecyclePolicy():
            return EcrAction(Actions.Read.GetLifecyclePolicy.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def GetLifecyclePolicyPreview():
            return EcrAction(Actions.Read.GetLifecyclePolicyPreview.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def GetRepositoryPolicy():
            return EcrAction(Actions.Read.GetRepositoryPolicy.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def ListTagsForResource():
            return EcrAction(Actions.Read.ListTagsForResource.__name__, EcrAction.Repository.__name__)

    class Write:
        @staticmethod
        def BatchDeleteImage():
            return EcrAction(Actions.Write.BatchDeleteImage.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def CompleteLayerUpload():
            return EcrAction(Actions.Write.CompleteLayerUpload.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def CreateRepository():
            return EcrAction(Actions.Write.CreateRepository.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def DeleteLifecyclePolicy():
            return EcrAction(Actions.Write.DeleteLifecyclePolicy.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def DeleteRepository():
            return EcrAction(Actions.Write.DeleteRepository.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def DeleteRepositoryPolicy():
            return EcrAction(Actions.Write.DeleteRepositoryPolicy.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def InitiateLayerUpload():
            return EcrAction(Actions.Write.InitiateLayerUpload.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def PutImage():
            return EcrAction(Actions.Write.PutImage.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def PutImageScanningConfiguration():
            return EcrAction(Actions.Write.PutImageScanningConfiguration.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def PutImageTagMutability():
            return EcrAction(Actions.Write.PutImageTagMutability.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def PutLifecyclePolicy():
            return EcrAction(Actions.Write.PutLifecyclePolicy.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def StartImageScan():
            return EcrAction(Actions.Write.StartImageScan.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def StartLifecyclePolicyPreview():
            return EcrAction(Actions.Write.StartLifecyclePolicyPreview.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def UploadLayerPart():
            return EcrAction(Actions.Write.UploadLayerPart.__name__, EcrAction.Repository.__name__)

    class List:
        @staticmethod
        def DescribeRepositories():
            return EcrAction(Actions.List.DescribeRepositories.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def ListImages():
            return EcrAction(Actions.List.ListImages.__name__, EcrAction.Repository.__name__)

    class PermissionsManagement:
        @staticmethod
        def SetRepositoryPolicy():
            return EcrAction(Actions.PermissionsManagement.SetRepositoryPolicy.__name__, EcrAction.Repository.__name__)

    class Tagging:
        @staticmethod
        def TagResource():
            return EcrAction(Actions.Tagging.TagResource.__name__, EcrAction.Repository.__name__)

        @staticmethod
        def UntagResource():
            return EcrAction(Actions.Tagging.UntagResource.__name__, EcrAction.Repository.__name__)

    @staticmethod
    def ReadAll():
        return EcrAccessLevelAllActions(Actions.Read)

    @staticmethod
    def WriteAll():
        return EcrAccessLevelAllActions(Actions.Write)

    @staticmethod
    def ListAll():
        return EcrAccessLevelAllActions(Actions.List)

    @staticmethod
    def TaggingAll():
        return EcrAccessLevelAllActions(Actions.Tagging)

    @staticmethod
    def PermissionManagementAll():
        return EcrAccessLevelAllActions(Actions.PermissionsManagement)
