from .model import Model
from .resource import Resource
from .parameter import Parameter
import json
import yaml


class Template(Model):
    def __init__(self, version: str):
        super(Template, self).__init__()
        self.AWSTemplateFormatVersion(version)

    def AWSTemplateFormatVersion(self, version: str):
        return self._set_field(self.AWSTemplateFormatVersion.__name__, version)

    def Description(self, description: str):
        return self._set_field(self.Description.__name__, description)

    def Parameters(self, *parameters: Parameter):
        if self._get_field(self.Parameters.__name__) is None:
            self._set_field(self.Parameters.__name__, {})

        for parameter in list(parameters):
            self._get_field(self.Parameters.__name__, {}).update(parameter.__to_dict__())

        return self

    '''
    def Mappings(self, *mappings: PyformationMapping):
        if self._get_field(self.Mappings.__name__) is None:
            self._set_field(self.Mappings.__name__, {})

        for mapping in list(mappings):
            self._get_field(self.Mappings.__name__, {}).update(mapping)

        return self
    '''

    def Resources(self, *resources: Resource):
        if self._get_field(self.Resources.__name__) is None:
            self._set_field(self.Resources.__name__, {})

        for resource in list(resources):
            self._get_field(self.Resources.__name__).update(resource.__to_dict__())

        return self

    def JSON(self, filename: str):
        json.dump(self.__to_dict__(), open("{}.json".format(filename), "w"))

    def YAML(self, filename: str):
        yaml.dump(json.loads(json.dumps(self.__to_dict__())), open("{}.yml".format(filename), "w"))

