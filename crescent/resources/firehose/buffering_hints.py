from crescent.core import Model
from .constants import ModelRequiredProperties


class BufferingHints(Model):
    def __init__(self):
        super(BufferingHints, self).__init__(
            min_value={self.IntervalInSeconds.__name__: 60,
                       self.SizeInMBs.__name__: 1},
            max_value={self.IntervalInSeconds.__name__: 900,
                       self.SizeInMBs.__name__: 128},
            required_properties=ModelRequiredProperties.BUFFERING_HINTS
        )

    def IntervalInSeconds(self, interval_in_secs: int):
        return self._set_field(self.IntervalInSeconds.__name__, interval_in_secs)

    def SizeInMBs(self, size_in_mbs: int):
        return self._set_field(self.SizeInMBs.__name__, size_in_mbs)
