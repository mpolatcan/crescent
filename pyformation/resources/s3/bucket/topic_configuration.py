from pyformation import PyformationModel
from .notification_filter import NotificationFilter


class TopicConfiguration(PyformationModel):
    def Event(self, value: str):
        return self._set_field(self.Event.__name__, value)

    def Filter(self, value: NotificationFilter):
        return self._set_field(self.Filter.__name__, value.__to_dict__())

    def Topic(self, value: str):
        return self._set_field(self.Topic.__name__, value)
