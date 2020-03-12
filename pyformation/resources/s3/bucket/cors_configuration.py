from pyformation import PyformationModel
from .cors_rule import CorsRule


class CorsConfiguration(PyformationModel):
    def CorsRules(self, *value: CorsRule):
        return self._set_field(self.CorsRules.__name__, [cr.__to_dict__() for cr in list(value)])
