from zepyhrus.core import Model, Validator


class AbortIncompleteMultipartUpload(Model):
    @Validator.validate(type=int)
    def DaysAfterInitiation(self, value: int):
        return self._set_field(self.DaysAfterInitiation.__name__, value)
