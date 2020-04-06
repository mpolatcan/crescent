from crescent.policy_builder import PolicyBuilder, Actions
from crescent import Ecr as ecr, Efs as efs
import json

json.dump(
    PolicyBuilder("test").AllowActions(
        Actions.Efs.List.DescribeFileSystem().FileSystem(efs.Arn.FileSystemArn("test")),
        Actions.Firehose.List.ListDeliveryStreams().AllResources(),
        Actions.Ecr.Read.DescribeImages().Repository(ecr.RepositoryArn("test")),
        Actions.Firehose.ListAll().AllResources()
    ).DenyActions(
        Actions.Efs.List.DescribeAccessPoints().FileSystem(efs.Arn.FileSystemArn("test")),
        Actions.Efs.Read.DescribeFileSystemPolicy().AllResources()
    ).Create(),
    open("policy.json", "w"),
    indent=2
)
