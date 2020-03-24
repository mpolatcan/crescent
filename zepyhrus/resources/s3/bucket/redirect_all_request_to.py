from zepyhrus.core import Model, Validator
from .constants import AllowedValues


class RedirectAllRequestTo(Model):
    @Validator.validate(type=str)
    def HostName(self, value: str):
        return self._set_field(self.HostName.__name__, value)

    @Validator.validate(type=str, allowed_values=AllowedValues.REDIRECT_ALL_REQUEST_TO_PROTOCOL)
    def Protocol(self, value: str):
        return self._set_field(self.Protocol.__name__, value)
