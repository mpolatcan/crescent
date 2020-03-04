from typing import List
from resources.shared.base_model import BaseModel
from resources.s3.bucket.storage_class_analysis import StorageClassAnalysis
from resources.s3.bucket.tag_filter import TagFilter


class AnalyticsConfiguration(BaseModel):
    __PROPERTY_ID = "Id"
    __PROPERTY_PREFIX = "Prefix"
    __PROPERTY_STORAGE_CLASS_ANALYSIS = "StorageClassAnalysis"
    __PROPERTY_TAG_FILTERS = "TagFilters"

    def id(self, value: str):
        return self._add_field(self.__PROPERTY_ID, value)

    def prefix(self, value: str):
        return self._add_field(self.__PROPERTY_PREFIX, value)

    def storage_class_analysis(self, value: StorageClassAnalysis):
        return self._add_field(self.__PROPERTY_STORAGE_CLASS_ANALYSIS, value)

    def tag_filters(self, value: List[TagFilter]):
        return self._add_field(self.__PROPERTY_TAG_FILTERS, [tag_filter.create() for tag_filter in value])
