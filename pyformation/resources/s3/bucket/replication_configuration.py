from pyformation.core import Model, Validator
from .replication_rule import ReplicationRule


class ReplicationConfiguration(Model):
    @Validator.validate(type=str)
    def Role(self, value: str):
        return self._set_field(self.Role.__name__, value)

    @Validator.validate(type=ReplicationRule)
    def Rules(self, *value: ReplicationRule):
        return self._set_field(self.Rules.__name__, [rr.__to_dict__() for rr in list(value)])
