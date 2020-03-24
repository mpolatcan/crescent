from zepyhrus.core import Validator
from .buffering_hints import BufferingHints


class ElasticsearchBufferingHints(BufferingHints):
    def __init__(self):
        super(ElasticsearchBufferingHints, self).__init__()

    @Validator.validate(type=int, min_value=60, max_value=900)
    def IntervalInSeconds(self, value: int):
        super().IntervalInSeconds(value)
        return self

    @Validator.validate(type=int, min_value=1, max_value=100)
    def SizeInMBs(self, value: int):
        super().SizeInMBs(value)
        return self
