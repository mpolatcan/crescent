from pyformation.core import Model, Validator


class LifecyclePolicy(Model):
    __PROPERTY_TRANSITION_TO_IA = "TransitionToIA"

    @Validator.validate(type=str)
    def TransitionToIA(self, value: str):
        return self._set_field(self.TransitionToIA.__name__, value)
