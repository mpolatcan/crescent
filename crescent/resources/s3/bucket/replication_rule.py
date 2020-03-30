from crescent.core import Model, Validator
from .replication_destination import ReplicationDestination
from .source_selection_criteria import SourceSelectionCriteria
from .constants import AllowedValues, ModelRequiredProperties


class ReplicationRule(Model):
    @Validator.validate(type=ReplicationDestination, required_properties=ModelRequiredProperties.REPLICATION_DESTINATION)
    def Destination(self, destination: ReplicationDestination):
        return self._set_field(self.Destination.__name__, destination.__to_dict__())

    @Validator.validate(type=str)
    def Id(self, id: str):
        return self._set_field(self.Id.__name__, id)

    @Validator.validate(type=str)
    def Prefix(self, prefix: str):
        return self._set_field(self.Prefix.__name__, prefix)

    @Validator.validate(type=SourceSelectionCriteria, required_properties=ModelRequiredProperties.SOURCE_SELECTION_CRITERIA)
    def SourceSelectionCriteria(self, source_selection_criteria: SourceSelectionCriteria):
        return self._set_field(self.SourceSelectionCriteria.__name__, source_selection_criteria.__to_dict__())

    @Validator.validate(type=str, allowed_values=AllowedValues.REPLICATION_RULE_STATUS)
    def Status(self, status: str):
        return self._set_field(self.Status.__name__, status)
