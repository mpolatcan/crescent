from pyformation import PyformationModel
from .replication_destination import ReplicationDestination
from .source_selection_criteria import SourceSelectionCriteria


class ReplicationRule(PyformationModel):
    def Destination(self, value: ReplicationDestination):
        return self._set_field(self.Destination.__name__, value.__to_dict__())

    def Id(self, value: str):
        return self._set_field(self.Id.__name__, value)

    def Prefix(self, value: str):
        return self._set_field(self.Prefix.__name__, value)

    def SourceSelectionCriteria(self, value: SourceSelectionCriteria):
        return self._set_field(self.SourceSelectionCriteria.__name__, value.__to_dict__())

    def Status(self, value: str):
        return self._set_field(self.Status.__name__, value)
