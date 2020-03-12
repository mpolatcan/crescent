from pyformation import PyformationModel
from .lambda_configuration import LambdaConfiguration
from .queue_configuration import QueueConfiguration
from .topic_configuration import TopicConfiguration


class NotificationConfiguration(PyformationModel):
    def LambdaConfigurations(self, *value: LambdaConfiguration):
        return self._set_field(self.LambdaConfigurations.__name__, [lc.__to_dict__() for lc in list(value)])

    def QueueConfigurations(self, *value: QueueConfiguration):
        return self._set_field(self.QueueConfigurations.__name__, [qc.__to_dict__() for qc in list(value)])

    def TopicConfigurations(self, *value: TopicConfiguration):
        return self._set_field(self.TopicConfigurations.__name__, [tc.__to_dict__() for tc in list(value)])
