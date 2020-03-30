from crescent.core import Model, Validator


class AbortIncompleteMultipartUpload(Model):
    @Validator.validate(type=int)
    def DaysAfterInitiation(self, days_after_initiation: int):
        return self._set_field(self.DaysAfterInitiation.__name__, days_after_initiation)
