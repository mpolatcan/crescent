from zepyhrus.core import Model, Validator


class BufferingHints(Model):
    @Validator.validate(type=int, min_value=60, max_value=900)
    def IntervalInSeconds(self, value: int):
        return self._set_field(self.IntervalInSeconds.__name__, value)

    @Validator.validate(type=int, min_value=1, max_value=128)
    def SizeInMBs(self, value: int):
        return self._set_field(self.SizeInMBs.__name__, value)
