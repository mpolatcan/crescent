from pyformation.core import Model, Validator
from .input_format_configuration import InputFormatConfiguration
from .output_format_configuration import OutputFormatConfiguration
from .schema_configuration import SchemaConfiguration


class DataFormatConversionConfiguration(Model):
    def Enabled(self, value: bool):
        return self._set_field(self.Enabled.__name__, value)

    @Validator.validate(type=InputFormatConfiguration)
    def InputFormatConfiguration(self, value: InputFormatConfiguration):
        return self._set_field(self.InputFormatConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=OutputFormatConfiguration)
    def OutputFormatConfiguration(self, value: OutputFormatConfiguration):
        return self._set_field(self.OutputFormatConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=SchemaConfiguration)
    def SchemaConfiguration(self, value: SchemaConfiguration):
        return self._set_field(self.SchemaConfiguration.__name__, value.__to_dict__())
