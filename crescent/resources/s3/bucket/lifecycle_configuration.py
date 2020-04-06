from crescent.core import Model
from .rule import Rule
from .constants import ModelRequiredProperties


class LifecycleConfiguration(Model):
    def __init__(self):
        super(LifecycleConfiguration, self).__init__(required_properties=ModelRequiredProperties.LIFECYCLE_CONFIGURATION)

    def Rules(self, *rules: Rule):
        return self._set_field(self.Rules.__name__, list(rules))
