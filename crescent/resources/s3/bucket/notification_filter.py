from crescent.core import Model
from .s3_key_filter import S3KeyFilter
from .constants import ModelRequiredProperties


class NotificationFilter(Model):
    def __init__(self):
        super(NotificationFilter, self).__init__(required_properties=ModelRequiredProperties.NOTIFICATION_FILTER)

    def S3Key(self, s3_key: S3KeyFilter):
        return self._set_field(self.S3Key.__name__, s3_key)
