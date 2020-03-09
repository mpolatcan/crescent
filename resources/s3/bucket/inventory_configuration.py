from resources.shared import BaseModel
from resources.s3.bucket import Destination


class InventoryConfiguration(BaseModel):
    __PROPERTY_DESTINATION = "Destination"
    __PROPERTY_ENABLED = "Enabled"
    __PROPERTY_ID = "Id"
    __PROPERTY_INCLUDED_OBJECT_VERSIONS = "IncludedObjectVersions"
    __PROPERTY_OPTIONAL_FIELDS = "OptionalFields"
    __PROPERTY_PREFIX = "Prefix"
    __PROPERTY_SCHEDULE_FREQUENCY = "ScheduleFrequency"

    def destination(self, value: Destination):
        return self._add_field(self.__PROPERTY_DESTINATION, value)

    def enabled(self, value: bool):
        return self._add_field(self.__PROPERTY_ENABLED, value)

    def id(self, value: str):
        return self._add_field(self.__PROPERTY_ID, value)

    def included_object_versions(self, value: str):
        return self._add_field(self.__PROPERTY_INCLUDED_OBJECT_VERSIONS, value)

    def optional_fields(self, *value: str):
        return self._add_field(self.__PROPERTY_OPTIONAL_FIELDS, list(value))

    def prefix(self, value: str):
        return self._add_field(self.__PROPERTY_PREFIX, value)

    def schedule_frequency(self, value: str):
        return self._add_field(self.__PROPERTY_SCHEDULE_FREQUENCY, value)

