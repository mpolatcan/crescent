from crescent.core import Model
from .lambda_configuration import LambdaConfiguration
from .queue_configuration import QueueConfiguration
from .topic_configuration import TopicConfiguration


class NotificationConfiguration(Model):
    def LambdaConfigurations(self, *lambda_confs: LambdaConfiguration):
        return self._set_field(self.LambdaConfigurations.__name__, list(lambda_confs))

    def QueueConfigurations(self, *queue_confs: QueueConfiguration):
        return self._set_field(self.QueueConfigurations.__name__, list(queue_confs))

    def TopicConfigurations(self, *topic_confs: TopicConfiguration):
        return self._set_field(self.TopicConfigurations.__name__, list(topic_confs))
