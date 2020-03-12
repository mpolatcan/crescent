from pyformation import PyformationModel
from .object_lock_rule import ObjectLockRule


class ObjectLockConfiguration(PyformationModel):
    def ObjectLockEnabled(self, value: bool):
        return self._set_field(self.ObjectLockEnabled.__name__, value)

    def Rule(self, value: ObjectLockRule):
        return self._set_field(self.Rule.__name__, value.__to_dict__())
