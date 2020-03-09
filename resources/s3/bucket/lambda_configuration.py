from resources.shared import BaseModel
from resources.s3.bucket import NotificationFilter


class LambdaConfiguration(BaseModel):
    __PROPERTY_EVENT = "Event"
    __PROPERTY_FILTER = "Filter"
    __PROPERTY_FUNCTION = "Function"

    def event(self, value: str):
        return self._add_field(self.__PROPERTY_EVENT, value)

    def filter(self, value: NotificationFilter):
        return self._add_field(self.__PROPERTY_FILTER, value.create())

    def function(self, value: str):
        return self._add_field(self.__PROPERTY_FUNCTION, value)
