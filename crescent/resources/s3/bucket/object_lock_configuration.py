from crescent.core import Model, Validator
from .object_lock_rule import ObjectLockRule


class ObjectLockConfiguration(Model):
    @Validator.validate(type=bool)
    def ObjectLockEnabled(self, object_lock_enabled: bool):
        return self._set_field(self.ObjectLockEnabled.__name__, "Enabled") if object_lock_enabled else self

    @Validator.validate(type=ObjectLockRule)
    def Rule(self, rule: ObjectLockRule):
        return self._set_field(self.Rule.__name__, rule.__to_dict__())
