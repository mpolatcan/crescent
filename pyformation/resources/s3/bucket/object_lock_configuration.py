from pyformation.resources.shared import BaseModel
from pyformation.resources.s3.bucket import ObjectLockRule


class ObjectLockConfiguration(BaseModel):
    __PROPERTY_OBJECT_LOCK_ENABLED = "ObjectLockEnabled"
    __PROPERTY_RULE = "Rule"

    def object_lock_enabled(self, value: bool):
        return self._add_field(self.__PROPERTY_OBJECT_LOCK_ENABLED, value)

    def rule(self, value: ObjectLockRule):
        return self._add_field(self.__PROPERTY_RULE, value)
