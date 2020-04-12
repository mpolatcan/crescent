from crescent.core import Model
from crescent.functions import AnyFn
from .constants import AllowedValues, ModelRequiredProperties
from typing import Union


class CorsRule(Model):
    def __init__(self):
        super(CorsRule, self).__init__(
            max_length={self.Id.__name__: 255},
            allowed_values={self.AllowedMethods.__name__: AllowedValues.ALLOWED_METHODS},
            required_properties=ModelRequiredProperties.CORS_RULE
        )

    def AllowedHeaders(self, *allowed_headers: Union[str, AnyFn]):
        return self._set_field(self.AllowedHeaders.__name__, list(allowed_headers))

    def AllowedMethods(self, *allowed_methods: Union[str, AnyFn]):
        return self._set_field(self.AllowedMethods.__name__, list(allowed_methods))

    def AllowedOrigins(self, *allowed_origins: Union[str, AnyFn]):
        return self._set_field(self.AllowedOrigins.__name__, list(allowed_origins))

    def ExposedHeaders(self, *exposed_headers: Union[str, AnyFn]):
        return self._set_field(self.ExposedHeaders.__name__, list(exposed_headers))

    def Id(self, id: Union[str, AnyFn]):
        return self._set_field(self.Id.__name__, id)

    def MaxAge(self, max_age: Union[int, AnyFn]):
        return self._set_field(self.MaxAge.__name__, max_age)
