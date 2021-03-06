from crescent.core import Model
from crescent.functions import AnyFn
from .constants import Conditions
from typing import Union


class CloudWatchLoggingOptions(Model):
    def __init__(self):
        super(CloudWatchLoggingOptions, self).__init__(conditions={
            self.Enabled.__name__: Conditions.CLOUDWATCH_LOGGING_OPTIONS_ENABLED
        })

    def Enabled(self, enabled: Union[bool, AnyFn]):
        return self._set_field(self.Enabled.__name__, enabled)

    def LogGroupName(self, log_group_name: Union[str, AnyFn]):
        return self._set_field(self.LogGroupName.__name__, log_group_name)

    def LogStreamName(self, log_stream_name: Union[str, AnyFn]):
        return self._set_field(self.LogStreamName.__name__, log_stream_name)
