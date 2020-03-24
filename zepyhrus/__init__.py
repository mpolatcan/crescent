from .core import *
from .resources import *


class ZepyhrusFactory:
    @staticmethod
    def Template(version: str = "2010-09-09"):
        return Template(version)

    @staticmethod
    def Parameter(id: str, data_type: str):
        return Parameter(id, data_type)

    @staticmethod
    def Tag(key: str, value: str):
        return Tag(key, value)


__all__ = [
    "ZepyhrusFactory",
    "types",
    "aws_types",
    "aws_ec2_types",
    "aws_ssm_types",
    "ecr",
    "efs",
    "efs_file_system",
    "efs_mount_target",
    "firehose",
    "firehose_delivery_stream",
    "iam",
    "kinesis",
    "kinesis_stream",
    "kinesis_stream_consumer",
    "s3",
    "s3_access_point",
    "s3_bucket",
    "s3_bucket_policy",
    "rds",
    "rds_cluster",
    "rds_instance",
    "rds_security_group",
    "rds_subnet_group",
    "rds_option_group",
    "rds_event_subscription"
]
