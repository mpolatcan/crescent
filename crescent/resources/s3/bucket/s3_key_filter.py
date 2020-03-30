from crescent.core import Model, Validator
from .filter_rule import FilterRule
from .constants import ModelRequiredProperties


class S3KeyFilter(Model):
    @Validator.validate(type=FilterRule, required_properties=ModelRequiredProperties.FILTER_RULE)
    def Rules(self, *rules: FilterRule):
        return self._set_field(self.Rules, [fr.__to_dict__() for fr in list(rules)])
