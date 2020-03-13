from pyformation.core import Model, Validator
from .notification_filter import NotificationFilter


class LambdaConfiguration(Model):
    @Validator.validate(type=str)
    def Event(self, value: str):
        return self._set_field(self.Event.__name__, value)

    @Validator.validate(type=NotificationFilter)
    def Filter(self, value: NotificationFilter):
        return self._set_field(self.Filter.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def Function(self, value: str):
        return self._set_field(self.Function.__name__, value)
