from resources.shared import BaseModel


class ProcessorParameter(BaseModel):
    __PROPERTY_PARAMETER_NAME = "ParameterName"
    __PROPERTY_PARAMETER_VALUE = "ParameterValue"

    def parameter_name(self, value: str):
        return self._add_field(self.__PROPERTY_PARAMETER_NAME, value)

    def parameter_value(self, value: str):
        return self._add_field(self.__PROPERTY_PARAMETER_VALUE, value)
