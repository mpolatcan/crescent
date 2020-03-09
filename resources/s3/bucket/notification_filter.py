from resources.shared import BaseModel
from resources.s3.bucket import S3KeyFilter


class NotificationFilter(BaseModel):
    __PROPERTY_S3KEY = "S3Key"

    def s3key(self, value: S3KeyFilter):
        return self._add_field(self.__PROPERTY_S3KEY, value.create())
