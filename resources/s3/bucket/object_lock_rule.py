from resources.shared.base_model import BaseModel
from resources.s3.bucket.default_retention import DefaultRetention


class ObjectLockRule(BaseModel):
    __PROPERTY_DEFAULT_RETENTION = "DefaultRetention"

    def default_retention(self, value: DefaultRetention):
        return self._add_field(self.__PROPERTY_DEFAULT_RETENTION, value.create())
