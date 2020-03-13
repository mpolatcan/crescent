from pyformation.core import Model, Validator


class BufferingHints(Model):
    @Validator.validate(type=int)
    def IntervalInSeconds(self, value: int):
        return self._set_field(self.IntervalInSeconds.__name__, value)

    @Validator.validate(type=int)
    def SizeInMBs(self, value: int):
        return self._set_field(self.SizeInMBs.__name__, value)
