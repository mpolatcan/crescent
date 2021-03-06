from crescent.core import Model
from crescent.functions import AnyFn
from .constants import AllowedValues, ModelRequiredProperties
from typing import Union


class RedirectAllRequestTo(Model):
    def __init__(self):
        super(RedirectAllRequestTo, self).__init__(
            allowed_values={self.Protocol.__name__: AllowedValues.REDIRECT_ALL_REQUEST_TO_PROTOCOL},
            required_properties=ModelRequiredProperties.REDIRECT_ALL_REQUEST_TO
        )

    def HostName(self, host_name: Union[str, AnyFn]):
        return self._set_field(self.HostName.__name__, host_name)

    def Protocol(self, protocol: Union[str, AnyFn]):
        return self._set_field(self.Protocol.__name__, protocol)
