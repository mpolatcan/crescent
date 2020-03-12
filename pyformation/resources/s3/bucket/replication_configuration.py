from pyformation import PyformationModel
from .replication_rule import ReplicationRule


class ReplicationConfiguration(PyformationModel):
    def Role(self, value: str):
        return self._set_field(self.Role.__name__, value)

    def Rules(self, *value: ReplicationRule):
        return self._set_field(self.Rules.__name__, [rr.__to_dict__() for rr in list(value)])
