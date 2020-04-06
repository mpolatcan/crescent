from crescent.core import Model
from .constants import AllowedValues, ModelRequiredProperties


class AccessControlTranslation(Model):
    def __init__(self):
        super(AccessControlTranslation, self).__init__(
            allowed_values={self.Owner.__name__: AllowedValues.OWNER},
            required_properties=ModelRequiredProperties.ACCESS_CONTROL_TRANSLATION
        )

    def Owner(self, owner: str):
        return self._set_field(self.Owner.__name__, owner)
