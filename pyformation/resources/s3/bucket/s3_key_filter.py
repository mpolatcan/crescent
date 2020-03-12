from pyformation import PyformationModel
from .filter_rule import FilterRule


class S3KeyFilter(PyformationModel):
    def Rules(self, *value: FilterRule):
        return self._set_field(self.Rules, [fr.__to_dict__() for fr in list(value)])
