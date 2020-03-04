from resources.shared.base_model import BaseModel


class LoggingConfiguration(BaseModel):
    __PROPERTY_DESTINATION_BUCKET_NAME = "DestinationBucketName"
    __PROPERTY_LOG_FILE_PREFIX = "LogFilePrefix"

    def destination_bucket_name(self, value: str):
        return self._add_field(self.__PROPERTY_DESTINATION_BUCKET_NAME, value)

    def log_file_prefix(self, value: str):
        return self._add_field(self.__PROPERTY_LOG_FILE_PREFIX, value)
