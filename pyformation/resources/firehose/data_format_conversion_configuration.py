from pyformation import PyformationModel
from .input_format_configuration import InputFormatConfiguration
from .output_format_configuration import OutputFormatConfiguration
from .schema_configuration import SchemaConfiguration


class DataFormatConversionConfiguration(PyformationModel):
    def Enabled(self, value: bool):
        return self._set_field(self.Enabled.__name__, value)

    def InputFormatConfiguration(self, value: InputFormatConfiguration):
        return self._set_field(self.InputFormatConfiguration.__name__, value.__to_dict__())

    def OutputFormatConfiguration(self, value: OutputFormatConfiguration):
        return self._set_field(self.OutputFormatConfiguration.__name__, value.__to_dict__())

    def SchemaConfiguration(self, value: SchemaConfiguration):
        return self._set_field(self.SchemaConfiguration.__name__, value.__to_dict__())
