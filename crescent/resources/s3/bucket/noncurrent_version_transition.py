from crescent.core import Model
from crescent.functions import AnyFn
from .constants import AllowedValues, ModelRequiredProperties
from typing import Union


class NoncurrentVersionTransition(Model):
    def __init__(self):
        super(NoncurrentVersionTransition, self).__init__(
            allowed_values={self.StorageClass.__name__: AllowedValues.NONCURRENT_VERSION_TRANSITION_SC},
            required_properties=ModelRequiredProperties.NONCURRENT_VERSION_TRANSITION
        )

    def StorageClass(self, storage_class: Union[str, AnyFn]):
        return self._set_field(self.StorageClass.__name__, storage_class)

    def TransitionInDays(self, transition_in_days: Union[int, AnyFn]):
        return self._set_field(self.TransitionInDays.__name__, transition_in_days)
