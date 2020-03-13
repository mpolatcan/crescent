from pyformation.core import Model, Validator
from .tag_filter import TagFilter


class MetricsConfiguration(Model):
    @Validator.validate(type=str)
    def Id(self, value: str):
        return self._set_field(self.Id.__name__, value)

    @Validator.validate(type=str)
    def Prefix(self, value: str):
        return self._set_field(self.Prefix.__name__, value)

    @Validator.validate(type=TagFilter)
    def TagFilters(self, *value: TagFilter):
        return self._set_field(self.TagFilters.__name__, [tf.__to_dict__() for tf in list(value)])
