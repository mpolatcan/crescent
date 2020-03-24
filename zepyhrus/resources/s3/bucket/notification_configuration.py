from zepyhrus.core import Model, Validator
from .lambda_configuration import LambdaConfiguration
from .queue_configuration import QueueConfiguration
from .topic_configuration import TopicConfiguration
from .constants import RequiredProperties


class NotificationConfiguration(Model):
    @Validator.validate(type=LambdaConfiguration, required_properties=RequiredProperties.LAMBDA_CONFIGURATION)
    def LambdaConfigurations(self, *value: LambdaConfiguration):
        return self._set_field(self.LambdaConfigurations.__name__, [lc.__to_dict__() for lc in list(value)])

    @Validator.validate(type=QueueConfiguration, required_properties=RequiredProperties.QUEUE_CONFIGURATION)
    def QueueConfigurations(self, *value: QueueConfiguration):
        return self._set_field(self.QueueConfigurations.__name__, [qc.__to_dict__() for qc in list(value)])

    @Validator.validate(type=TopicConfiguration, required_properties=RequiredProperties.TOPIC_CONFIGURATION)
    def TopicConfigurations(self, *value: TopicConfiguration):
        return self._set_field(self.TopicConfigurations.__name__, [tc.__to_dict__() for tc in list(value)])
