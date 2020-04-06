from crescent.core import Model
from .filter_rule import FilterRule
from .constants import ModelRequiredProperties


class S3KeyFilter(Model):
    def __init__(self):
        super(S3KeyFilter, self).__init__(required_properties=ModelRequiredProperties.S3_KEY_FILTER)

    def Rules(self, *rules: FilterRule):
        return self._set_field(self.Rules, list(rules))
