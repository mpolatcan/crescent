from crescent.core import Model, Validator


class BufferingHints(Model):
    @Validator.validate(type=int, min_value=60, max_value=900)
    def IntervalInSeconds(self, interval_in_secs: int):
        return self._set_field(self.IntervalInSeconds.__name__, interval_in_secs)

    @Validator.validate(type=int, min_value=1, max_value=128)
    def SizeInMBs(self, size_in_mbs: int):
        return self._set_field(self.SizeInMBs.__name__, size_in_mbs)
