from crescent.core import Model, Validator
from .constants import AllowedValues


class Transition(Model):
    @Validator.validate(type=str, allowed_values=AllowedValues.TRANSITION_SC)
    def StorageClass(self, storage_class: str):
        return self._set_field(self.StorageClass.__name__, storage_class)

    @Validator.validate(type=str)
    def TransitionDate(self, transition_date: str):
        return self._set_field(self.TransitionDate.__name__, transition_date)

    @Validator.validate(type=int)
    def TransitionInDays(self, transition_in_days: int):
        return self._set_field(self.TransitionInDays.__name__, transition_in_days)
