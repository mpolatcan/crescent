from typing import List
from resources.shared.base_model import BaseModel
from resources.s3.bucket.lambda_configuration import LambdaConfiguration
from resources.s3.bucket.queue_configuration import QueueConfiguration
from resources.s3.bucket.topic_configuration import TopicConfiguration


class NotificationConfiguration(BaseModel):
    __PROPERTY_LAMBDA_CONFIGURATIONS = "LambdaConfigurations"
    __PROPERTY_QUEUE_CONFIGURATIONS = "QueueConfigurations"
    __PROPERTY_TOPIC_CONFIGURATIONS = "TopicConfigurations"

    def lambda_configurations(self, value: List[LambdaConfiguration]):
        return self._add_field(self.__PROPERTY_LAMBDA_CONFIGURATIONS, [
            lambda_conf.create() for lambda_conf in value
        ])

    def queue_configurations(self, value: List[QueueConfiguration]):
        return self._add_field(self.__PROPERTY_QUEUE_CONFIGURATIONS, [
            queue_conf.create() for queue_conf in value
        ])

    def topic_configurations(self, value: List[TopicConfiguration]):
        return self._add_field(self.__PROPERTY_QUEUE_CONFIGURATIONS, [
            topic_conf.create() for topic_conf in value
        ])