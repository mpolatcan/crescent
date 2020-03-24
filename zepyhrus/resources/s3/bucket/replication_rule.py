from zepyhrus.core import Model, Validator
from .replication_destination import ReplicationDestination
from .source_selection_criteria import SourceSelectionCriteria
from .constants import AllowedValues, RequiredProperties


class ReplicationRule(Model):
    @Validator.validate(type=ReplicationDestination, required_properties=RequiredProperties.REPLICATION_DESTINATION)
    def Destination(self, value: ReplicationDestination):
        return self._set_field(self.Destination.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def Id(self, value: str):
        return self._set_field(self.Id.__name__, value)

    @Validator.validate(type=str)
    def Prefix(self, value: str):
        return self._set_field(self.Prefix.__name__, value)

    @Validator.validate(type=SourceSelectionCriteria, required_properties=RequiredProperties.SOURCE_SELECTION_CRITERIA)
    def SourceSelectionCriteria(self, value: SourceSelectionCriteria):
        return self._set_field(self.SourceSelectionCriteria.__name__, value.__to_dict__())

    @Validator.validate(type=str, allowed_values=AllowedValues.REPLICATION_RULE_STATUS)
    def Status(self, value: str):
        return self._set_field(self.Status.__name__, value)
