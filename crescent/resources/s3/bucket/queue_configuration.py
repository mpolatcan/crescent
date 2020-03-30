from crescent.core import Model, Validator
from .notification_filter import NotificationFilter
from .constants import ModelRequiredProperties


class QueueConfiguration(Model):
    @Validator.validate(type=str)
    def Event(self, event: str):
        return self._set_field(self.Event.__name__, event)

    @Validator.validate(type=NotificationFilter, required_properties=ModelRequiredProperties.NOTIFICATION_FILTER)
    def Filter(self, filter: NotificationFilter):
        return self._set_field(self.Filter.__name__, filter.__to_dict__())

    @Validator.validate(type=str)
    def Queue(self, queue: str):
        return self._set_field(self.Queue.__name__, queue)
