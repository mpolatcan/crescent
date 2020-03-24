from zepyhrus.core import Model, Validator
from .notification_filter import NotificationFilter
from .constants import RequiredProperties


class TopicConfiguration(Model):
    @Validator.validate(type=str)
    def Event(self, value: str):
        return self._set_field(self.Event.__name__, value)

    @Validator.validate(type=NotificationFilter, required_properties=RequiredProperties.NOTIFICATION_FILTER)
    def Filter(self, value: NotificationFilter):
        return self._set_field(self.Filter.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def Topic(self, value: str):
        return self._set_field(self.Topic.__name__, value)
