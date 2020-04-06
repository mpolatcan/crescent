from crescent.core import Model
from .replication_destination import ReplicationDestination
from .source_selection_criteria import SourceSelectionCriteria
from .constants import AllowedValues, ModelRequiredProperties


class ReplicationRule(Model):
    def __init__(self):
        super(ReplicationRule, self).__init__(
            allowed_values={self.Status.__name__: AllowedValues.REPLICATION_RULE_STATUS},
            required_properties=ModelRequiredProperties.REPLICATION_RULE
        )

    def Destination(self, destination: ReplicationDestination):
        return self._set_field(self.Destination.__name__, destination)

    def Id(self, id: str):
        return self._set_field(self.Id.__name__, id)

    def Prefix(self, prefix: str):
        return self._set_field(self.Prefix.__name__, prefix)

    def SourceSelectionCriteria(self, source_selection_criteria: SourceSelectionCriteria):
        return self._set_field(self.SourceSelectionCriteria.__name__, source_selection_criteria)

    def Status(self, status: str):
        return self._set_field(self.Status.__name__, status)
