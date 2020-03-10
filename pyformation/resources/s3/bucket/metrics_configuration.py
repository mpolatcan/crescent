from pyformation.resources.shared import BaseModel
from pyformation.resources.s3.bucket import TagFilter


class MetricsConfiguration(BaseModel):
    __PROPERTY_ID = "Id"
    __PROPERTY_PREFIX = "Prefix"
    __PROPERTY_TAG_FILTERS = "TagFilters"

    def id(self, value: str):
        return self._add_field(self.__PROPERTY_ID, value)

    def prefix(self, value: str):
        return self._add_field(self.__PROPERTY_PREFIX, value)

    def tag_filters(self, *value: TagFilter):
        return self._add_field(self.__PROPERTY_TAG_FILTERS, [
            tag_filter for tag_filter in list(value)
        ])
