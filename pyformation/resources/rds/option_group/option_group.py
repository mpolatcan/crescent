from pyformation.core import Resource, Tag, Validator
from .option_configuration import OptionConfiguration


class OptionGroup(Resource):
    __TYPE = "AWS::RDS::OptionGroup"

    def __init__(self, id: str):
        super(OptionGroup, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def EngineName(self, value: str):
        return self._set_property(self.EngineName.__name__, value)

    @Validator.validate(type=str)
    def MajorEngineVersion(self, value: str):
        return self._set_property(self.MajorEngineVersion.__name__, value)

    @Validator.validate(type=OptionConfiguration)
    def OptionConfigurations(self, *value: OptionConfiguration):
        return self._set_property(self.OptionConfigurations.__name__, [oc.__to_dict__() for oc in list(value)])

    @Validator.validate(type=str)
    def OptionGroupDescription(self, value: str):
        return self._set_property(self.OptionGroupDescription.__name__, value)

    @Validator.validate(type=Tag)
    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))
