from crescent.core import Model
from crescent.functions import AnyFn
from .constants import ModelRequiredProperties
from typing import Union


class ElasticsearchBufferingHints(Model):
    def __init__(self):
        super(ElasticsearchBufferingHints, self).__init__(
            min_value={self.IntervalInSeconds.__name__: 60,
                       self.SizeInMBs.__name__: 1},
            max_value={self.IntervalInSeconds.__name__: 900,
                       self.SizeInMBs.__name__: 100},
            required_propertieS=ModelRequiredProperties.ELASTICSEARCH_BUFFERING_HINTS
        )

    def IntervalInSeconds(self, interval_in_secs: Union[int, AnyFn]):
        return self._set_field(self.IntervalInSeconds.__name__, interval_in_secs)

    def SizeInMBs(self, size_in_mbs: Union[int, AnyFn]):
        return self._set_field(self.SizeInMBs.__name__, size_in_mbs)
