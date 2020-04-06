from crescent.core import Model
from .constants import AllowedValues, ModelRequiredProperties


class NoncurrentVersionTransition(Model):
    def __init__(self):
        super(NoncurrentVersionTransition, self).__init__(
            allowed_values={self.StorageClass.__name__: AllowedValues.NONCURRENT_VERSION_TRANSITION_SC},
            required_properties=ModelRequiredProperties.NONCURRENT_VERSION_TRANSITION
        )

    def StorageClass(self, storage_class: str):
        return self._set_field(self.StorageClass.__name__, storage_class)

    def TransitionInDays(self, transition_in_days: int):
        return self._set_field(self.TransitionInDays.__name__, transition_in_days)
