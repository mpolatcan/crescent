from .pyformation_model import PyformationModel
from .pyformation_resource import PyformationResource
from .pyformation_parameter import PyformationParameter
from .pyformation_template import PyformationTemplate
from .tag import Tag

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
    firehose= FirehoseFactory()
    iam = IamFactory()
    kinesis = KinesisFactory()
    s3 = S3Factory()
    rds = RdsFactory()

    @staticmethod
    def Template(version: str):
        return PyformationTemplate(version)

    @staticmethod
    def Parameter(id: str, data_type: str):
        return PyformationParameter(id, data_type)

    @staticmethod
    def Tag(key: str, value: str):
        return Tag(key, value)


__all__ = [
    "PyformationFactory",
    "PyformationTemplate",
    "PyformationResource",
    "PyformationParameter",
    "PyformationModel",
    "Tag"
]
