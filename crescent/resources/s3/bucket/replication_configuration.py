from crescent.core import Model
from .replication_rule import ReplicationRule
from .constants import ModelRequiredProperties


class ReplicationConfiguration(Model):
    def __init__(self):
        super(ReplicationConfiguration, self).__init__(required_properties=ModelRequiredProperties.REPLICATION_CONFIGURATION)

    def Role(self, role: str):
        return self._set_field(self.Role.__name__, role)

    def Rules(self, *rules: ReplicationRule):
        return self._set_field(self.Rules.__name__, list(rules))
