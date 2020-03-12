from pyformation import PyformationModel


class ProcessorParameter(PyformationModel):
    def ParameterName(self, value: str):
        return self._set_field(self.ParameterName.__name__, value)

    def ParameterValue(self, value: str):
        return self._set_field(self.ParameterValue.__name__, value)
