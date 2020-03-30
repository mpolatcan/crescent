from crescent.core import Model, Validator
from .constants import AllowedValues


class RedirectAllRequestTo(Model):
    @Validator.validate(type=str)
    def HostName(self, host_name: str):
        return self._set_field(self.HostName.__name__, host_name)

    @Validator.validate(type=str, allowed_values=AllowedValues.REDIRECT_ALL_REQUEST_TO_PROTOCOL)
    def Protocol(self, protocol: str):
        return self._set_field(self.Protocol.__name__, protocol)
