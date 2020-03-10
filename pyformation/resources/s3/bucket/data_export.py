from pyformation.resources.shared import BaseModel
from pyformation.resources.s3.bucket import Destination


class DataExport(BaseModel):
    __PROPERTY_DESTINATION = "Destination"
    __PROPERTY_OUTPUT_SCHEMA_VERSION = "OutputSchemaVersion"

    def destination(self, value: Destination):
        return self._add_field(self.__PROPERTY_DESTINATION, value)

    def output_schema_version(self, value: str):
        return self._add_field(self.__PROPERTY_OUTPUT_SCHEMA_VERSION, value)
