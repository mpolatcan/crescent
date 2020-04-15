from .action import Action
from .ecr import Actions as EcrActions
from .efs import Actions as EfsActions
from .firehose import Actions as FirehoseActions
from .kinesis import Actions as KinesisActions
from .rds import Actions as RdsActions

# TODO All Actions will be added


class Actions:
    Ecr = EcrActions
    Efs = EfsActions
    Firehose = FirehoseActions
    Kinesis = KinesisActions
    Rds = RdsActions


__all__ = ["Action", "Actions"]
