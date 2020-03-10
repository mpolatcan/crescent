from pyformation.resources.shared import BaseModel
from pyformation.resources.s3.bucket import ReplicationDestination, SourceSelectionCriteria


class ReplicationRule(BaseModel):
    __PROPERTY_DESTINATION = "Destination"
    __PROPERTY_ID = "Id"
    __PROPERTY_PREFIX = "Prefix"
    __PROPERTY_SOURCE_SELECTION_CRITERIA = "SourceSelectionCriteria"
    __PROPERTY_STATUS = "Status"

    def destination(self, value: ReplicationDestination):
        return self._add_field(self.__PROPERTY_DESTINATION, value)

    def id(self, value: str):
        return self._add_field(self.__PROPERTY_ID, value)

    def prefix(self, value: str):
        return self._add_field(self.__PROPERTY_PREFIX, value)

    def source_selection_criteria(self, value: SourceSelectionCriteria):
        return self._add_field(self.__PROPERTY_SOURCE_SELECTION_CRITERIA, value)

    def status(self, value: str):
        return self._add_field(self.__PROPERTY_STATUS, value)
