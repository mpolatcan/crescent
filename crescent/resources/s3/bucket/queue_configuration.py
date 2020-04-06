from crescent.core import Model
from .notification_filter import NotificationFilter
from .constants import ModelRequiredProperties


class QueueConfiguration(Model):
    def __init__(self):
        super(QueueConfiguration, self).__init__(required_properties=ModelRequiredProperties.QUEUE_CONFIGURATION)

    def Event(self, event: str):
        return self._set_field(self.Event.__name__, event)

    def Filter(self, filter: NotificationFilter):
        return self._set_field(self.Filter.__name__, filter)

    def Queue(self, queue: str):
        return self._set_field(self.Queue.__name__, queue)
