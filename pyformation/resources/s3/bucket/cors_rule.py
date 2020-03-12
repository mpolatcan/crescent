from pyformation import PyformationModel


class CorsRule(PyformationModel):
    def AllowedHeaders(self, *value: str):
        return self._set_field(self.AllowedHeaders.__name__, list(value))

    def AllowedMethods(self, *value: str):
        return self._set_field(self.AllowedMethods.__name__, list(value))

    def AllowedOrigins(self, *value: str):
        return self._set_field(self.AllowedOrigins.__name__, list(value))

    def ExposedHeaders(self, *value: str):
        return self._set_field(self.ExposedHeaders.__name__, list(value))

    def Id(self, value: str):
        return self._set_field(self.Id.__name__, value)

    def MaxAge(self, value: int):
        return self._set_field(self.MaxAge.__name__, value)
