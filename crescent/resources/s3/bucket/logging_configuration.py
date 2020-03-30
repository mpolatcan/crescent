from crescent.core import Model, Validator


class LoggingConfiguration(Model):
    @Validator.validate(type=str)
    def DestinationBucketName(self, destination_bucket_name: str):
        return self._set_field(self.DestinationBucketName.__name__, destination_bucket_name)

    @Validator.validate(type=str)
    def LogFilePrefix(self, log_file_prefix: str):
        return self._set_field(self.LogFilePrefix.__name__, log_file_prefix)
