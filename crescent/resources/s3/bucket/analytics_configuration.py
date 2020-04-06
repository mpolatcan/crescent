from crescent.core import Model
from .storage_class_analysis import StorageClassAnalysis
from .tag_filter import TagFilter
from .constants import ModelRequiredProperties


class AnalyticsConfiguration(Model):
    def __init__(self):
        super(AnalyticsConfiguration, self).__init__(required_properties=ModelRequiredProperties.ANALYTICS_CONFIGURATION)

    def Id(self, id: str):
        return self._set_field(self.Id.__name__, id)

    def Prefix(self, prefix: str):
        return self._set_field(self.Prefix.__name__, prefix)

    def StorageClassAnalysis(self, storage_class_analysis: StorageClassAnalysis):
        return self._set_field(self.StorageClassAnalysis.__name__, storage_class_analysis)

    def TagFilters(self, *tag_filters: TagFilter):
        return self._set_field(self.TagFilters.__name__, list(tag_filters))
