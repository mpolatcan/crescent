from pyformation.core import Model, Validator


class SplunkRetryOptions(Model):
    @Validator.validate(type=int, min_value=0, max_value=7200)
    def DurationInSeconds(self, value: int):
        return self._set_field(self.DurationInSeconds.__name__, value)
