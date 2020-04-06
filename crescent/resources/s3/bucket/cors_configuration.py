from crescent.core import Model
from .cors_rule import CorsRule
from .constants import ModelRequiredProperties


class CorsConfiguration(Model):
    def __init__(self):
        super(CorsConfiguration, self).__init__(required_properties=ModelRequiredProperties.CORS_CONFIGURATION)

    def CorsRules(self, *cors_rules: CorsRule):
        return self._set_field(self.CorsRules.__name__, list(cors_rules))
