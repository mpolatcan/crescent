from crescent.core import Model
from .constants import AllowedValues


class RouteSettings(Model):
    def __init__(self):
        super(RouteSettings, self).__init__(
            allowed_values={self.LoggingLevel.__name__: AllowedValues.LOGGING_LEVEL}
        )

    def DataTraceEnabled(self, data_trace_enabled: bool):
        return self._set_field(self.DataTraceEnabled.__name__, data_trace_enabled)

    def DetailedMetricsEnabled(self, detailed_metrics_enabled: bool):
        return self._set_field(self.DetailedMetricsEnabled.__name__, detailed_metrics_enabled)

    def LoggingLevel(self, logging_level: str):
        return self._set_field(self.LoggingLevel.__name__, logging_level)

    def ThrottlingBurstLimit(self, throttling_burst_limit: int):
        return self._set_field(self.ThrottlingBurstLimit.__name__, throttling_burst_limit)

    def ThrottlingRateLimit(self, throttling_rate_limit: float):
        return self._set_field(self.ThrottlingRateLimit.__name__, throttling_rate_limit)
