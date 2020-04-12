from crescent.core import Model
from crescent.functions import AnyFn
from .notification_filter import NotificationFilter
from .constants import ModelRequiredProperties
from typing import Union


class LambdaConfiguration(Model):
    def __init__(self):
        super(LambdaConfiguration, self).__init__(required_properties=ModelRequiredProperties.LAMBDA_CONFIGURATION)

    def Event(self, event: Union[str, AnyFn]):
        return self._set_field(self.Event.__name__, event)

    def Filter(self, filter: NotificationFilter):
        return self._set_field(self.Filter.__name__, filter)

    def Function(self, function: Union[str, AnyFn]):
        return self._set_field(self.Function.__name__, function)
