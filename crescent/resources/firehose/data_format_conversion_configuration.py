from crescent.core import Model
from .input_format_configuration import InputFormatConfiguration
from .output_format_configuration import OutputFormatConfiguration
from .schema_configuration import SchemaConfiguration
from .constants import ModelRequiredProperties


class DataFormatConversionConfiguration(Model):
    def __init__(self):
        super(DataFormatConversionConfiguration, self).__init__(
            required_properties=ModelRequiredProperties.DATA_FORMAT_CONVERSION_CONFIGURATION
        )

    def Enabled(self, enabled: bool):
        return self._set_field(self.Enabled.__name__, enabled)

    def InputFormatConfiguration(self, input_format_conf: InputFormatConfiguration):
        return self._set_field(self.InputFormatConfiguration.__name__, input_format_conf)

    def OutputFormatConfiguration(self, output_format_conf: OutputFormatConfiguration):
        return self._set_field(self.OutputFormatConfiguration.__name__, output_format_conf)

    def SchemaConfiguration(self, schema_conf: SchemaConfiguration):
        return self._set_field(self.SchemaConfiguration.__name__, schema_conf)
