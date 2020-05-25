from crescent.functions import AnyFn
from .processor import Processor
from .processor_parameter import ProcessorParameter
from .constants import ProcessorType
from typing import Union


class LambdaProcessor(Processor):
    def __init__(self):
        super(LambdaProcessor, self).__init__()
        self.Type(ProcessorType.LAMBDA)

    def LambdaArn(self, lambda_arn: Union[str, AnyFn]):
        return self.Parameters(ProcessorParameter().ParameterName(self.LambdaArn.__name__).ParameterValue(lambda_arn))

    def BufferSizeInMBs(self, buffer_size_in_mbs: Union[str, AnyFn]):
        return self.Parameters(ProcessorParameter().ParameterName(self.BufferSizeInMBs.__name__).ParameterValue(buffer_size_in_mbs))

    def BufferIntervalInSeconds(self, buffer_interval_in_secs: Union[str, AnyFn]):
        return self.Parameters(ProcessorParameter().ParameterName(self.BufferIntervalInSeconds.__name__).ParameterValue(buffer_interval_in_secs))

    def NumberOfRetries(self, number_of_retries: Union[str, AnyFn]):
        return self.Parameters(ProcessorParameter().ParameterName(self.NumberOfRetries.__name__).ParameterValue(number_of_retries))

    def RoleArn(self, role_arn: Union[str, AnyFn]):
        return self.Parameters(ProcessorParameter().ParameterName(self.RoleArn.__name__).ParameterValue(role_arn))
