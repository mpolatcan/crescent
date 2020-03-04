from resources.shared.base_model import BaseModel
from resources.s3.bucket.notification_filter import NotificationFilter


class QueueConfiguration(BaseModel):
    __PROPERTY_EVENT = "Event"
    __PROPERTY_FILTER = "Filter"
    __PROPERTY_QUEUE = "Queue"

    def event(self, value: str):
        return self._add_field(self.__PROPERTY_EVENT, value)

    def filter(self, value: NotificationFilter):
        return self._add_field(self.__PROPERTY_FILTER, value.create())

    def queue(self, value: str):
        return self._add_field(self.__PROPERTY_QUEUE, value)
