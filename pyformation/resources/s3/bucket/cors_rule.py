from pyformation.core import Model, Validator


class CorsRule(Model):
    @Validator.validate(type=str)
    def AllowedHeaders(self, *value: str):
        return self._set_field(self.AllowedHeaders.__name__, list(value))

    @Validator.validate(type=str)
    def AllowedMethods(self, *value: str):
        return self._set_field(self.AllowedMethods.__name__, list(value))

    @Validator.validate(type=str)
    def AllowedOrigins(self, *value: str):
        return self._set_field(self.AllowedOrigins.__name__, list(value))

    @Validator.validate(type=str)
    def ExposedHeaders(self, *value: str):
        return self._set_field(self.ExposedHeaders.__name__, list(value))

    @Validator.validate(type=str)
    def Id(self, value: str):
        return self._set_field(self.Id.__name__, value)

    @Validator.validate(type=int)
    def MaxAge(self, value: int):
        return self._set_field(self.MaxAge.__name__, value)
