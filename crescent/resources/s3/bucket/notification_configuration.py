from crescent.core import Model, Validator
from .lambda_configuration import LambdaConfiguration
from .queue_configuration import QueueConfiguration
from .topic_configuration import TopicConfiguration
from .constants import ModelRequiredProperties


class NotificationConfiguration(Model):
    @Validator.validate(type=LambdaConfiguration, required_properties=ModelRequiredProperties.LAMBDA_CONFIGURATION)
    def LambdaConfigurations(self, *lambda_confs: LambdaConfiguration):
        return self._set_field(self.LambdaConfigurations.__name__, [lc.__to_dict__() for lc in list(lambda_confs)])

    @Validator.validate(type=QueueConfiguration, required_properties=ModelRequiredProperties.QUEUE_CONFIGURATION)
    def QueueConfigurations(self, *queue_confs: QueueConfiguration):
        return self._set_field(self.QueueConfigurations.__name__, [qc.__to_dict__() for qc in list(queue_confs)])

    @Validator.validate(type=TopicConfiguration, required_properties=ModelRequiredProperties.TOPIC_CONFIGURATION)
    def TopicConfigurations(self, *topic_confs: TopicConfiguration):
        return self._set_field(self.TopicConfigurations.__name__, [tc.__to_dict__() for tc in list(topic_confs)])
