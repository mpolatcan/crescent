from pyformation import PyformationModel
from .notification_filter import NotificationFilter


class LambdaConfiguration(PyformationModel):
    def Event(self, value: str):
        return self._set_field(self.Event.__name__, value)

    def Filter(self, value: NotificationFilter):
        return self._set_field(self.Filter.__name__, value.__to_dict__())

    def Function(self, value: str):
        return self._set_field(self.Function.__name__, value)
