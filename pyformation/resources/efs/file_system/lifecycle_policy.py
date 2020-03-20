from pyformation.core import Model, Validator


class LifecyclePolicy(Model):
    __PROPERTY_TRANSITION_TO_IA = "TransitionToIA"

    @Validator.validate(type=str, allowed_values=[
        "AFTER_14_DAYS", "AFTER_30_DAYS", "AFTER_60_DAYS", "AFTER_7_DAYS", "AFTER_90_DAYS"
    ])
    def TransitionToIA(self, value: str):
        return self._set_field(self.TransitionToIA.__name__, value)
