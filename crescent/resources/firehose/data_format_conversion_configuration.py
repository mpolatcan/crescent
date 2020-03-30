from crescent.core import Model, Validator
from .input_format_configuration import InputFormatConfiguration
from .output_format_configuration import OutputFormatConfiguration
from .schema_configuration import SchemaConfiguration
from .constants import ModelRequiredProperties


class DataFormatConversionConfiguration(Model):
    def Enabled(self, enabled: bool):
        return self._set_field(self.Enabled.__name__, enabled)

    @Validator.validate(type=InputFormatConfiguration, required_properties=ModelRequiredProperties.INPUT_FORMAT_CONFIGURATION)
    def InputFormatConfiguration(self, input_format_conf: InputFormatConfiguration):
        return self._set_field(self.InputFormatConfiguration.__name__, input_format_conf.__to_dict__())

    @Validator.validate(type=OutputFormatConfiguration, required_properties=ModelRequiredProperties.OUTPUT_FORMAT_CONFIGURATION)
    def OutputFormatConfiguration(self, output_format_conf: OutputFormatConfiguration):
        return self._set_field(self.OutputFormatConfiguration.__name__, output_format_conf.__to_dict__())

    @Validator.validate(type=SchemaConfiguration, required_properties=ModelRequiredProperties.SCHEMA_CONFIGURATION)
    def SchemaConfiguration(self, schema_conf: SchemaConfiguration):
        return self._set_field(self.SchemaConfiguration.__name__, schema_conf.__to_dict__())
