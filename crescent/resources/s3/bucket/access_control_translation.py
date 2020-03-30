from crescent.core import Model, Validator
from .constants import AllowedValues


class AccessControlTranslation(Model):
    @Validator.validate(type=str, allowed_values=AllowedValues.OWNER)
    def Owner(self, owner: str):
        return self._set_field(self.Owner.__name__, owner)
