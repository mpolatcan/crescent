from typing import List
from resources.shared import BaseModel
from resources.s3.bucket import ServerSideEncryptionRule


class BucketEncryption(BaseModel):
    __PROPERTY_SERVER_SIDE_ENCRYPTION_CONFIGURATION = "ServerSideEncryptionConfiguration"

    def server_side_encryption_configuration(self, value: List[ServerSideEncryptionRule]):
        return self._add_field(self.__PROPERTY_SERVER_SIDE_ENCRYPTION_CONFIGURATION, [
            sse_rule.create() for sse_rule in value
        ])
