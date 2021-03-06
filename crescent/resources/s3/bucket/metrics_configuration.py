from crescent.core import Model
from crescent.functions import AnyFn
from .tag_filter import TagFilter
from .constants import ModelRequiredProperties
from typing import Union


class MetricsConfiguration(Model):
    def __init__(self):
        super(MetricsConfiguration, self).__init__(required_properties=ModelRequiredProperties.METRICS_CONFIGURATION)

    def Id(self, id: Union[str, AnyFn]):
        return self._set_field(self.Id.__name__, id)

    def Prefix(self, prefix: Union[str, AnyFn]):
        return self._set_field(self.Prefix.__name__, prefix)

    def TagFilters(self, *tag_filters: TagFilter):
        return self._set_field(self.TagFilters.__name__, list(tag_filters))
