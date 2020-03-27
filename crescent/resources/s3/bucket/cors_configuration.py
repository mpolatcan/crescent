from crescent.core import Model, Validator
from .cors_rule import CorsRule
from .constants import ModelRequiredProperties


class CorsConfiguration(Model):
    @Validator.validate(type=CorsRule, required_properties=ModelRequiredProperties.CORS_RULE)
    def CorsRules(self, *value: CorsRule):
        return self._set_field(self.CorsRules.__name__, [cr.__to_dict__() for cr in list(value)])
