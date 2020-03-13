from .core import (
    Template,
    Parameter,
    Tag
)

from .resources import (
    EcrFactory,
    EfsFactory,
    FirehoseFactory,
    IamFactory,
    KinesisFactory,
    S3Factory,
    RdsFactory
)


class PyformationFactory:
    ecr = EcrFactory()
    efs = EfsFactory()
    firehose = FirehoseFactory()
    iam = IamFactory()
    kinesis = KinesisFactory()
    s3 = S3Factory()
    rds = RdsFactory()

    @staticmethod
    def Template(version: str):
        return Template(version)

    @staticmethod
    def Parameter(id: str, data_type: str):
        return Parameter(id, data_type)

    @staticmethod
    def Tag(key: str, value: str):
        return Tag(key, value)


__all__ = [
    "PyformationFactory"
]
