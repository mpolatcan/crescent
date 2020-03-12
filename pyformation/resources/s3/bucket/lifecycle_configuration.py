from pyformation import PyformationModel
from .rule import Rule


class LifecycleConfiguration(PyformationModel):
    def Rules(self, *value: Rule):
        return self._set_field(self.Rules.__name__, [rule.__to_dict__() for rule in list(value)])
