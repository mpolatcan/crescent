from pyformation import PyformationModel
from .storage_class_analysis import StorageClassAnalysis
from .tag_filter import TagFilter


class AnalyticsConfiguration(PyformationModel):
    def Id(self, value: str):
        return self._set_field(self.Id.__name__, value)

    def Prefix(self, value: str):
        return self._set_field(self.Prefix.__name__, value)

    def StorageClassAnalysis(self, value: StorageClassAnalysis):
        return self._set_field(self.StorageClassAnalysis.__name__, value.__to_dict__())

    def TagFilters(self, *value: TagFilter):
        return self._set_field(self.TagFilters.__name__, [tf.__to_dict__() for tf in list(value)])
