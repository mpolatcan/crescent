from pyformation.core import Model, Validator
from .filter_rule import FilterRule
from .constants import RequiredProperties


class S3KeyFilter(Model):
    @Validator.validate(type=FilterRule, required_properties=RequiredProperties.FILTER_RULE)
    def Rules(self, *value: FilterRule):
        return self._set_field(self.Rules, [fr.__to_dict__() for fr in list(value)])
