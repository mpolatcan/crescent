from zepyhrus.core import Model, Validator
from .object_lock_rule import ObjectLockRule


class ObjectLockConfiguration(Model):
    @Validator.validate(type=bool)
    def ObjectLockEnabled(self, value: bool):
        return self._set_field(self.ObjectLockEnabled.__name__, "Enabled") if value else self

    @Validator.validate(type=ObjectLockRule)
    def Rule(self, value: ObjectLockRule):
        return self._set_field(self.Rule.__name__, value.__to_dict__())
