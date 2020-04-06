from crescent.core import Model
from .default_retention import DefaultRetention


class ObjectLockRule(Model):
    def DefaultRetention(self, default_retention: DefaultRetention):
        return self._set_field(self.DefaultRetention.__name__, default_retention)
