from crescent.core import Model
from crescent.functions import AnyFn
from .constants import AllowedValues, ModelRequiredProperties
from typing import Union


class Transition(Model):
    def __init__(self):
        super(Transition, self).__init__(
            allowed_values={self.StorageClass.__name__: AllowedValues.TRANSITION_SC},
            required_properties=ModelRequiredProperties.TRANSITION
        )

    def StorageClass(self, storage_class: Union[str, AnyFn]):
        return self._set_field(self.StorageClass.__name__, storage_class)

    def TransitionDate(self, transition_date: Union[str, AnyFn]):
        return self._set_field(self.TransitionDate.__name__, transition_date)

    def TransitionInDays(self, transition_in_days: Union[int, AnyFn]):
        return self._set_field(self.TransitionInDays.__name__, transition_in_days)
