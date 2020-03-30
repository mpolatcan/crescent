from crescent.core import Model, Validator
from .storage_class_analysis import StorageClassAnalysis
from .tag_filter import TagFilter
from .constants import ModelRequiredProperties


class AnalyticsConfiguration(Model):
    @Validator.validate(type=str)
    def Id(self, id: str):
        return self._set_field(self.Id.__name__, id)

    @Validator.validate(type=str)
    def Prefix(self, prefix: str):
        return self._set_field(self.Prefix.__name__, prefix)

    @Validator.validate(type=StorageClassAnalysis)
    def StorageClassAnalysis(self, storage_class_analysis: StorageClassAnalysis):
        return self._set_field(self.StorageClassAnalysis.__name__, storage_class_analysis.__to_dict__())

    @Validator.validate(type=TagFilter, required_properties=ModelRequiredProperties.TAG_FILTER)
    def TagFilters(self, *tag_filters: TagFilter):
        return self._set_field(self.TagFilters.__name__, [tf.__to_dict__() for tf in list(tag_filters)])
