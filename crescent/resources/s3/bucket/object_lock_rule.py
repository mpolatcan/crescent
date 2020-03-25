from crescent.core import Model, Validator
from .default_retention import DefaultRetention


class ObjectLockRule(Model):
    @Validator.validate(type=DefaultRetention)
    def DefaultRetention(self, value: DefaultRetention):
        return self._set_field(self.DefaultRetention.__name__, value.__to_dict__())
