from pyformation.resources.shared import BaseModel
from pyformation.resources.s3.bucket import DefaultRetention


class ObjectLockRule(BaseModel):
    __PROPERTY_DEFAULT_RETENTION = "DefaultRetention"

    def default_retention(self, value: DefaultRetention):
        return self._add_field(self.__PROPERTY_DEFAULT_RETENTION, value)
