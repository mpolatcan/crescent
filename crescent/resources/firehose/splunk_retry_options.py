from crescent.core import Model, Validator


class SplunkRetryOptions(Model):
    @Validator.validate(type=int, min_value=0, max_value=7200)
    def DurationInSeconds(self, duration_in_secs: int):
        return self._set_field(self.DurationInSeconds.__name__, duration_in_secs)
