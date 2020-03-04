from resources.shared.base_model import BaseModel
from resources.s3.bucket.object_lock_rule import ObjectLockRule


class ObjectLockConfiguration(BaseModel):
    __PROPERTY_OBJECT_LOCK_ENABLED = "ObjectLockEnabled"
    __PROPERTY_RULE = "Rule"

    def object_lock_enabled(self, value: bool):
        return self._add_field(self.__PROPERTY_OBJECT_LOCK_ENABLED, value)

    def rule(self, value: ObjectLockRule):
        return self._add_field(self.__PROPERTY_RULE, value.create())
