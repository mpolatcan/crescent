from crescent.core import Model
from .constants import ModelRequiredProperties


class ElasticsearchRetryOptions(Model):
    def __init__(self):
        super(ElasticsearchRetryOptions, self).__init__(
            min_value={self.DurationInSeconds.__name__: 0},
            max_value={self.DurationInSeconds.__name__: 7200},
            required_properties=ModelRequiredProperties.ELASTICSEARCH_RETRY_OPTIONS
        )

    def DurationInSeconds(self, duration_in_secs: int):
        return self._set_field(self.DurationInSeconds.__name__, duration_in_secs)
