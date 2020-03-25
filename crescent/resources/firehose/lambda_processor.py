from crescent.core import Validator
from .processor import Processor
from .processor_parameter import ProcessorParameter
from .constants import ProcessorType


class LambdaProcessor(Processor):
    def __init__(self):
        super(LambdaProcessor, self).__init__()
        self.Type(ProcessorType.LAMBDA)

    @Validator.validate(type=str)
    def LambdaArn(self, value: str):
        return self.Parameters(ProcessorParameter().ParameterName(self.LambdaArn.__name__).ParameterValue(value))

    @Validator.validate(type=str)
    def BufferSizeInMBs(self, value: str):
        return self.Parameters(ProcessorParameter().ParameterName(self.BufferSizeInMBs.__name__).ParameterValue(value))

    @Validator.validate(type=str)
    def BufferIntervalInSeconds(self, value: str):
        return self.Parameters(ProcessorParameter().ParameterName(self.BufferIntervalInSeconds.__name__).ParameterValue(value))

    @Validator.validate(type=str)
    def NumberOfRetries(self, value: str):
        return self.Parameters(ProcessorParameter().ParameterName(self.NumberOfRetries.__name__).ParameterValue(value))

    @Validator.validate(type=str)
    def RoleArn(self, value: str):
        return self.Parameters(ProcessorParameter().ParameterName(self.RoleArn.__name__).ParameterValue(value))
