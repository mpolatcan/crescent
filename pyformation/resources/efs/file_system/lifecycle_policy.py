from pyformation.core import Model, Validator
from .constants import AllowedValues


class LifecyclePolicy(Model):
    @Validator.validate(type=str, allowed_values=AllowedValues.TRANSITION_TO_IA)
    def TransitionToIA(self, value: str):
        return self._set_field(self.TransitionToIA.__name__, value)
