from crescent.core import Model
from crescent.functions import AnyFn
from .constants import ModelRequiredProperties
from typing import Union


class SplunkRetryOptions(Model):
    def __init__(self):
        super(SplunkRetryOptions, self).__init__(
            min_value={self.DurationInSeconds.__name__: 0},
            max_value={self.DurationInSeconds.__name__: 7200},
            required_properties=ModelRequiredProperties.SPLUNK_RETRY_OPTIONS
        )

    def DurationInSeconds(self, duration_in_secs: Union[int, AnyFn]):
        return self._set_field(self.DurationInSeconds.__name__, duration_in_secs)
