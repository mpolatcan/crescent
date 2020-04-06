from crescent.core import Model
from .constants import AllowedValues, ModelRequiredProperties


class LifecyclePolicy(Model):
    def __init__(self):
        super(LifecyclePolicy, self).__init__(
            allowed_values={self.TransitionToIA.__name__: AllowedValues.TRANSITION_TO_IA},
            required_properties=ModelRequiredProperties.LIFECYCLE_POLICY
        )

    def TransitionToIA(self, transition_to_ia: str):
        return self._set_field(self.TransitionToIA.__name__, transition_to_ia)
