from pyformation.core import Model, Validator
from .s3_key_filter import S3KeyFilter


class NotificationFilter(Model):
    @Validator.validate(type=S3KeyFilter)
    def S3Key(self, value: S3KeyFilter):
        return self._set_field(self.S3Key.__name__, value.__to_dict__())
