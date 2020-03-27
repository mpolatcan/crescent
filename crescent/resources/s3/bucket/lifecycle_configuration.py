from crescent.core import Model, Validator
from .rule import Rule
from .constants import Conditions, ModelRequiredProperties


class LifecycleConfiguration(Model):
    @Validator.validate(type=Rule, required_properties=ModelRequiredProperties.RULE, conditions=Conditions.RULE)
    def Rules(self, *value: Rule):
        return self._set_field(self.Rules.__name__, [rule.__to_dict__() for rule in value])
