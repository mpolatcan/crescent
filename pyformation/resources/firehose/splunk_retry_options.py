from pyformation.core import Model, Validator


class SplunkRetryOptions(Model):
    @Validator.validate(type=int)
    def DurationInSeconds(self, value: int):
        return self._set_field(self.DurationInSeconds.__name__, value)
