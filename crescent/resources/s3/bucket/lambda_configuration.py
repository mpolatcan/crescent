from crescent.core import Model
from .notification_filter import NotificationFilter
from .constants import ModelRequiredProperties


class LambdaConfiguration(Model):
    def __init__(self):
        super(LambdaConfiguration, self).__init__(required_properties=ModelRequiredProperties.LAMBDA_CONFIGURATION)

    def Event(self, event: str):
        return self._set_field(self.Event.__name__, event)

    def Filter(self, filter: NotificationFilter):
        return self._set_field(self.Filter.__name__, filter)

    def Function(self, function: str):
        return self._set_field(self.Function.__name__, function)
