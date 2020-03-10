from pyformation.resources.shared import BaseModel
from pyformation.resources.s3.bucket import LambdaConfiguration, QueueConfiguration, TopicConfiguration


class NotificationConfiguration(BaseModel):
    __PROPERTY_LAMBDA_CONFIGURATIONS = "LambdaConfigurations"
    __PROPERTY_QUEUE_CONFIGURATIONS = "QueueConfigurations"
    __PROPERTY_TOPIC_CONFIGURATIONS = "TopicConfigurations"

    def lambda_configurations(self, *value: LambdaConfiguration):
        return self._add_field(self.__PROPERTY_LAMBDA_CONFIGURATIONS, [
            lambda_conf for lambda_conf in list(value)
        ])

    def queue_configurations(self, *value: QueueConfiguration):
        return self._add_field(self.__PROPERTY_QUEUE_CONFIGURATIONS, [
            queue_conf for queue_conf in list(value)
        ])

    def topic_configurations(self, *value: TopicConfiguration):
        return self._add_field(self.__PROPERTY_QUEUE_CONFIGURATIONS, [
            topic_conf for topic_conf in list(value)
        ])
