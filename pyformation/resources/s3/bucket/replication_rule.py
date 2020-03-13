from pyformation.core import Model, Validator
from .replication_destination import ReplicationDestination
from .source_selection_criteria import SourceSelectionCriteria


class ReplicationRule(Model):
    @Validator.validate(type=ReplicationDestination)
    def Destination(self, value: ReplicationDestination):
        return self._set_field(self.Destination.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def Id(self, value: str):
        return self._set_field(self.Id.__name__, value)

    @Validator.validate(type=str)
    def Prefix(self, value: str):
        return self._set_field(self.Prefix.__name__, value)

    @Validator.validate(type=SourceSelectionCriteria)
    def SourceSelectionCriteria(self, value: SourceSelectionCriteria):
        return self._set_field(self.SourceSelectionCriteria.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def Status(self, value: str):
        return self._set_field(self.Status.__name__, value)
