from crescent.core import Model
from crescent.functions import AnyFn
from .storage_class_analysis import StorageClassAnalysis
from .tag_filter import TagFilter
from .constants import ModelRequiredProperties
from typing import Union


class AnalyticsConfiguration(Model):
    def __init__(self):
        super(AnalyticsConfiguration, self).__init__(required_properties=ModelRequiredProperties.ANALYTICS_CONFIGURATION)

    def Id(self, id: Union[str, AnyFn]):
        return self._set_field(self.Id.__name__, id)

    def Prefix(self, prefix: Union[str, AnyFn]):
        return self._set_field(self.Prefix.__name__, prefix)

    def StorageClassAnalysis(self, storage_class_analysis: StorageClassAnalysis):
        return self._set_field(self.StorageClassAnalysis.__name__, storage_class_analysis)

    def TagFilters(self, *tag_filters: TagFilter):
        return self._set_field(self.TagFilters.__name__, list(tag_filters))
