from crescent.core import Model, Validator
from .constants import AllowedValues


class NoncurrentVersionTransition(Model):
    @Validator.validate(type=str, allowed_values=AllowedValues.NONCURRENT_VERSION_TRANSITION_SC)
    def StorageClass(self, storage_class: str):
        return self._set_field(self.StorageClass.__name__, storage_class)

    @Validator.validate(type=int)
    def TransitionInDays(self, transition_in_days: int):
        return self._set_field(self.TransitionInDays.__name__, transition_in_days)
