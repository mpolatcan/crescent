from crescent.core import Model
from .constants import ModelRequiredProperties


class AbortIncompleteMultipartUpload(Model):
    def __init__(self):
        super(AbortIncompleteMultipartUpload, self).__init__(
            required_properties=ModelRequiredProperties.ABORT_INCOMPLETE_MULTIPART_UPLOAD
        )

    def DaysAfterInitiation(self, days_after_initiation: int):
        return self._set_field(self.DaysAfterInitiation.__name__, days_after_initiation)
