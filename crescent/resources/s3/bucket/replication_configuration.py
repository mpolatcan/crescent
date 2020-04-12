from crescent.core import Model
from crescent.functions import AnyFn
from .replication_rule import ReplicationRule
from .constants import ModelRequiredProperties
from typing import Union


class ReplicationConfiguration(Model):
    def __init__(self):
        super(ReplicationConfiguration, self).__init__(required_properties=ModelRequiredProperties.REPLICATION_CONFIGURATION)

    def Role(self, role: Union[str, AnyFn]):
        return self._set_field(self.Role.__name__, role)

    def Rules(self, *rules: ReplicationRule):
        return self._set_field(self.Rules.__name__, list(rules))
