from .action import Action
from .ecr import Actions as EcrActions
from .efs import Actions as EfsActions

# TODO All Actions will be added


class Actions:
    Ecr = EcrActions
    Efs = EfsActions


__all__ = [
    "Action",
    "Actions"
]
