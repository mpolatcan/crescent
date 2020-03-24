from .model import Model
from .resource import Resource
from .parameter import Parameter
from .validator import Validator
import json
import yaml
from .constants import RequiredProperties


class Template(Model):
    def __init__(self, version: str):
        super(Template, self).__init__()
        self._set_field("AWSTemplateFormatVersion", version)

    @Validator.validate(type=str)
    def Description(self, description: str):
        return self._set_field(self.Description.__name__, description)

    @Validator.validate(type=Parameter)
    def Parameters(self, *parameters: Parameter):
        if self._get_field(self.Parameters.__name__) is None:
            self._set_field(self.Parameters.__name__, {})

        for parameter in list(parameters):
            self._get_field(self.Parameters.__name__, {}).update(parameter.__to_dict__())

        return self

    @Validator.validate(type=Resource, required_properties=RequiredProperties)
    def Resources(self, *resources: Resource):
        if self._get_field(self.Resources.__name__) is None:
            self._set_field(self.Resources.__name__, {})

        for resource in list(resources):
            self._get_field(self.Resources.__name__).update(resource.__to_dict__())

        return self

    @Validator.validate(type=str)
    def JSON(self, filename: str):
        json.dump(self.__to_dict__(), open("{}.json".format(filename), "w"))

    @Validator.validate(type=str)
    def YAML(self, filename: str):
        yaml.dump(json.loads(json.dumps(self.__to_dict__())), open("{}.yml".format(filename), "w"))

