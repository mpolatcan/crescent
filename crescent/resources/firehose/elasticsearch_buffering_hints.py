from crescent.core import Validator
from .buffering_hints import BufferingHints


class ElasticsearchBufferingHints(BufferingHints):
    def __init__(self):
        super(ElasticsearchBufferingHints, self).__init__()

    @Validator.validate(type=int, min_value=60, max_value=900)
    def IntervalInSeconds(self, interval_in_secs: int):
        super().IntervalInSeconds(interval_in_secs)
        return self

    @Validator.validate(type=int, min_value=1, max_value=100)
    def SizeInMBs(self, size_in_mbs: int):
        super().SizeInMBs(size_in_mbs)
        return self
