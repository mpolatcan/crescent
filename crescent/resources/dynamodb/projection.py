from crescent.core import Model
from .constants import AllowedValues


class Projection(Model):
    def __init__(self):
        super(Projection, self).__init__(
            allowed_values={self.ProjectionType.__name__: AllowedValues.PROJECTION_TYPE}
        )

    def NonKeyAttributes(self, *nonkey_attrs: str):
        return self._set_field(self.NonKeyAttributes.__name__, list(nonkey_attrs))

    def ProjectionType(self, projection_type: str):
        return self._set_field(self.ProjectionType.__name__, projection_type)