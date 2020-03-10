from pyformation.resources.shared import BaseModel
from pyformation.resources.firehose import InputFormatConfiguration, OutputFormatConfiguration, SchemaConfiguration


class DataFormatConversionConfiguration(BaseModel):
    __PROPERTY_ENABLED = "Enabled"
    __PROPERTY_INPUT_FORMAT_CONFIGURATION = "InputFormatConfiguration"
    __PROPERTY_OUTPUT_FORMAT_CONFIGURATION = "OutputFormatConfiguration"
    __PROPERTY_SCHEMA_CONFIGURATION = "SchemaConfiguration"

    def enabled(self, value: bool):
        return self._add_field(self.__PROPERTY_ENABLED, value)

    def input_format_configuration(self, value: InputFormatConfiguration):
        return self._add_field(self.__PROPERTY_INPUT_FORMAT_CONFIGURATION, value)

    def output_format_configuration(self, value: OutputFormatConfiguration):
        return self._add_field(self.__PROPERTY_OUTPUT_FORMAT_CONFIGURATION, value)

    def schema_configuration(self, value: SchemaConfiguration):
        return self._add_field(self.__PROPERTY_SCHEMA_CONFIGURATION, value)
