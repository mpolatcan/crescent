from pyformation.core import Model, Validator
from .rule import Rule


class LifecycleConfiguration(Model):
    @Validator.validate(type=Rule)
    def Rules(self, *value: Rule):
        return self._set_field(self.Rules.__name__, [rule.__to_dict__() for rule in list(value)])
