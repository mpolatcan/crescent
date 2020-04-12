from crescent.core import Model
from crescent.functions import AnyFn
from typing import Union


class LoggingConfiguration(Model):
    def DestinationBucketName(self, destination_bucket_name: Union[str, AnyFn]):
        return self._set_field(self.DestinationBucketName.__name__, destination_bucket_name)

    def LogFilePrefix(self, log_file_prefix: Union[str, AnyFn]):
        return self._set_field(self.LogFilePrefix.__name__, log_file_prefix)
