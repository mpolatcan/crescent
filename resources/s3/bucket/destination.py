from resources.shared import BaseModel


class Destination(BaseModel):
    __PROPERTY_BUCKET_ACCOUNT_ID = "BucketAccountId"
    __PROPERTY_BUCKET_ARN = "BucketArn"
    __PROPERTY_FORMAT = "Format"
    __PROPERTY_PREFIX = "Prefix"

    def bucket_account_id(self, value: str):
        return self._add_field(self.__PROPERTY_BUCKET_ACCOUNT_ID, value)

    def bucket_arn(self, value: str):
        return self._add_field(self.__PROPERTY_BUCKET_ARN, value)

    def format(self, value: str):
        return self._add_field(self.__PROPERTY_FORMAT, value)

    def prefix(self, value: str):
        return self._add_field(self.__PROPERTY_PREFIX, value)
