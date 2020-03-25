# TODO Validations will be checked and updated
from .model import Model
from .validator import Validator
from .resource_attrs import (
    CreationPolicy,
    DeletionPolicy,
    UpdatePolicy,
    UpdateReplacePolicy
)


class Resource(Model):
    __KEY_TYPE = "Type"
    __KEY_PROPERTIES = "Properties"

    def __init__(self, id: str, type: str):
        super(Resource, self).__init__()
        self._data[id] = {
            self.__KEY_TYPE: type,
            self.__KEY_PROPERTIES: {}
        }
        self._properties = self._data[id][self.__KEY_PROPERTIES]

    def _set_property(self, property, value):
        self._properties[property] = value

        return self

    def __get_properties__(self):
        return self._properties

    @Validator.validate(type=CreationPolicy)
    def CreationPolicy(self, value: CreationPolicy):
        return self._set_field(self.CreationPolicy.__name__, value.__to_dict__())

    @Validator.validate(type=str, allowed_values=[DeletionPolicy.SNAPSHOT,
                                                  DeletionPolicy.RETAIN,
                                                  DeletionPolicy.DELETE])
    def DeletionPolicy(self, value: str):
        return self._set_field(self.DeletionPolicy.__name__, value)

    @Validator.validate(type=str)
    def DependsOn(self, *value: str):
        return self._set_field(self.DependsOn.__name__, list(value))

    def Metadata(self, *value):
        if self._get_field(self.Metadata.__name__) is None:
            self._set_field(self.Metadata.__name__, {})

        for metadata in list(value):
            self._get_field(self.Metadata.__name__).update(metadata)

        return self

    @Validator.validate(type=UpdatePolicy)
    def UpdatePolicy(self, value: UpdatePolicy):
        return self._set_field(self.UpdatePolicy.__name__, value.__to_dict__())

    @Validator.validate(type=str, allowed_values=[UpdateReplacePolicy.SNAPSHOT,
                                                  UpdateReplacePolicy.RETAIN,
                                                  UpdateReplacePolicy.DELETE])
    def UpdateReplacePolicy(self, value: str):
        return self._set_field(self.UpdateReplacePolicy.__name__, value)
