from crescent.core import Model
from .constants import AllowedValues, ModelRequiredProperties


class CorsRule(Model):
    def __init__(self):
        super(CorsRule, self).__init__(
            max_length={self.Id.__name__: 255},
            allowed_values={self.AllowedMethods.__name__: AllowedValues.ALLOWED_METHODS},
            required_properties=ModelRequiredProperties.CORS_RULE
        )

    def AllowedHeaders(self, *allowed_headers: str):
        return self._set_field(self.AllowedHeaders.__name__, list(allowed_headers))

    def AllowedMethods(self, *allowed_methods: str):
        return self._set_field(self.AllowedMethods.__name__, list(allowed_methods))

    def AllowedOrigins(self, *allowed_origins: str):
        return self._set_field(self.AllowedOrigins.__name__, list(allowed_origins))

    def ExposedHeaders(self, *exposed_headers: str):
        return self._set_field(self.ExposedHeaders.__name__, list(exposed_headers))

    def Id(self, id: str):
        return self._set_field(self.Id.__name__, id)

    def MaxAge(self, max_age: int):
        return self._set_field(self.MaxAge.__name__, max_age)
