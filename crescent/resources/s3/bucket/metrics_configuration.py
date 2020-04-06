from crescent.core import Model
from .tag_filter import TagFilter
from .constants import ModelRequiredProperties


class MetricsConfiguration(Model):
    def __init__(self):
        super(MetricsConfiguration, self).__init__(required_properties=ModelRequiredProperties.METRICS_CONFIGURATION)

    def Id(self, id: str):
        return self._set_field(self.Id.__name__, id)

    def Prefix(self, prefix: str):
        return self._set_field(self.Prefix.__name__, prefix)

    def TagFilters(self, *tag_filters: TagFilter):
        return self._set_field(self.TagFilters.__name__, list(tag_filters))
