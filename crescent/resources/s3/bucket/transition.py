from crescent.core import Model
from .constants import AllowedValues, ModelRequiredProperties


class Transition(Model):
    def __init__(self):
        super(Transition, self).__init__(
            allowed_values={self.StorageClass.__name__: AllowedValues.TRANSITION_SC},
            required_properties=ModelRequiredProperties.TRANSITION
        )

    def StorageClass(self, storage_class: str):
        return self._set_field(self.StorageClass.__name__, storage_class)

    def TransitionDate(self, transition_date: str):
        return self._set_field(self.TransitionDate.__name__, transition_date)

    def TransitionInDays(self, transition_in_days: int):
        return self._set_field(self.TransitionInDays.__name__, transition_in_days)
