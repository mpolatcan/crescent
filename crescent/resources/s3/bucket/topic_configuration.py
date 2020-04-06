from crescent.core import Model
from .notification_filter import NotificationFilter
from .constants import ModelRequiredProperties


class TopicConfiguration(Model):
    def __init__(self):
        super(TopicConfiguration, self).__init__(required_properties=ModelRequiredProperties.TOPIC_CONFIGURATION)

    def Event(self, event: str):
        return self._set_field(self.Event.__name__, event)

    def Filter(self, filter: NotificationFilter):
        return self._set_field(self.Filter.__name__, filter)

    def Topic(self, topic: str):
        return self._set_field(self.Topic.__name__, topic)
