from crescent.core import Model
from .object_lock_rule import ObjectLockRule


class ObjectLockConfiguration(Model):
    def ObjectLockEnabled(self, object_lock_enabled: bool):
        return self._set_field(self.ObjectLockEnabled.__name__, "Enabled") if object_lock_enabled else self

    def Rule(self, rule: ObjectLockRule):
        return self._set_field(self.Rule.__name__, rule)
