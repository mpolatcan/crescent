from crescent.core import Model, Validator
from .s3_key_filter import S3KeyFilter
from .constants import ModelRequiredProperties


class NotificationFilter(Model):
    @Validator.validate(type=S3KeyFilter, required_properties=ModelRequiredProperties.S3_KEY_FILTER)
    def S3Key(self, value: S3KeyFilter):
        return self._set_field(self.S3Key.__name__, value.__to_dict__())
