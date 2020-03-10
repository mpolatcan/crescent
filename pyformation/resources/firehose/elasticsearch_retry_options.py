from pyformation.resources.shared import BaseModel


class ElasticsearchRetryOptions(BaseModel):
    __PROPERTY_DURATION_IN_SECONDS = "DurationInSeconds"

    def duration_in_seconds(self, value: int):
        return self._add_field(self.__PROPERTY_DURATION_IN_SECONDS, value)
