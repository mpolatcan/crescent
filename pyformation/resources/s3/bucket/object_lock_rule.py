from pyformation import PyformationModel
from .default_retention import DefaultRetention


class ObjectLockRule(PyformationModel):
    def DefaultRetention(self, value: DefaultRetention):
        return self._set_field(self.DefaultRetention.__name__, value.__to_dict__())
