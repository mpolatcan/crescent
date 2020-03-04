from resources.shared.base_model import BaseModel
from resources.s3.bucket.s3_key_filter import S3KeyFilter


class NotificationFilter(BaseModel):
    __PROPERTY_S3KEY = "S3Key"

    def s3key(self, value: S3KeyFilter):
        return self._add_field(self.__PROPERTY_S3KEY, value.create())
