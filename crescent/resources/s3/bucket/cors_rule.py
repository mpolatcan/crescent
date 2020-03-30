from crescent.core import Model, Validator
from .constants import AllowedValues


class CorsRule(Model):
    @Validator.validate(type=str)
    def AllowedHeaders(self, *allowed_headers: str):
        return self._set_field(self.AllowedHeaders.__name__, list(allowed_headers))

    @Validator.validate(type=str, allowed_values=AllowedValues.ALLOWED_METHODS)
    def AllowedMethods(self, *allowed_methods: str):
        return self._set_field(self.AllowedMethods.__name__, list(allowed_methods))

    @Validator.validate(type=str)
    def AllowedOrigins(self, *allowed_origins: str):
        return self._set_field(self.AllowedOrigins.__name__, list(allowed_origins))

    @Validator.validate(type=str)
    def ExposedHeaders(self, *exposed_headers: str):
        return self._set_field(self.ExposedHeaders.__name__, list(exposed_headers))

    @Validator.validate(type=str, max_length=255)
    def Id(self, id: str):
        return self._set_field(self.Id.__name__, id)

    @Validator.validate(type=int)
    def MaxAge(self, max_age: int):
        return self._set_field(self.MaxAge.__name__, max_age)
