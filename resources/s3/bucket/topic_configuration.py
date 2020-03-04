from resources.shared.base_model import BaseModel
from resources.s3.bucket.notification_filter import NotificationFilter


class TopicConfiguration(BaseModel):
    __PROPERTY_EVENT = "Event"
    __PROPERTY_FILTER = "Filter"
    __PROPERTY_TOPIC = "Topic"

    def event(self, value: str):
        return self._add_field(self.__PROPERTY_EVENT, value)

    def filter(self, value: NotificationFilter):
        return self._add_field(self.__PROPERTY_FILTER, value.create())

    def topic(self, value: str):
        return self._add_field(self.__PROPERTY_TOPIC, value)
