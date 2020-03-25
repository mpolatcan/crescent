from crescent.core import Model, Validator
from .rule import Rule
from .constants import Conditions, RequiredProperties


class LifecycleConfiguration(Model):
    @Validator.validate(type=Rule, required_properties=RequiredProperties.RULE, conditions=Conditions.RULE)
    def Rules(self, *value: Rule):
        return self._set_field(self.Rules.__name__, [rule.__to_dict__() for rule in value])
