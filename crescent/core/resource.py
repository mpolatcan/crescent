"""
    Resource JSON structure
    {
        <ID>: {
            "Type: <RESOURCE_TYPE>,
            "Properties": {
                ...
            },
            "CreationPolicy": {},
            "DeletionPolicy: "",
            "UpdatePolicy": {},
            "UpdateReplacePolicy": ""
        }
    }
"""
from crescent.functions import AnyFn
from .model import Model
from .constants import get_values
from .resource_attrs import CreationPolicy, DeletionPolicy, UpdatePolicy, UpdateReplacePolicy
from .metadata import Metadata
from typing import Union


class Resource(Model):
    __KEY_TYPE = "Type"
    __KEY_PROPERTIES = "Properties"
    __KEY_ALLOWED_VALUES = "allowed_values"
    __RESOURCE_VALIDATIONS_ALLOWED_VALUES = {
        DeletionPolicy.__name__: get_values(DeletionPolicy),
        UpdateReplacePolicy.__name__: get_values(UpdateReplacePolicy)
    }

    def __init__(self, id: str, type: str, **validations):
        # Add common resource properties validations
        if validations.get(self.__KEY_ALLOWED_VALUES, None):
            validations[self.__KEY_ALLOWED_VALUES].update(self.__RESOURCE_VALIDATIONS_ALLOWED_VALUES)
        else:
            validations[self.__KEY_ALLOWED_VALUES] = self.__RESOURCE_VALIDATIONS_ALLOWED_VALUES

        super(Resource, self).__init__(**validations)

        self.__id = id
        self._set_field(self.__id, {
            self.__KEY_TYPE: type,
            self.__KEY_PROPERTIES: {}
        })
        self._properties = self.__get_field__(self.__id)[self.__KEY_PROPERTIES]

    def _set_property(self, property, value):
        self.__get_field__(self.__id)[self.__KEY_PROPERTIES][property] = value
        return self

    def __set_common_property(self, property, value):
        self.__get_field__(self.__id)[property] = value
        return self

    def Condition(self, condition_id: Union[str, AnyFn]):
        return self.__set_common_property(self.Condition.__name__, condition_id)

    def CreationPolicy(self, creation_policy: CreationPolicy):
        return self.__set_common_property(self.CreationPolicy.__name__, creation_policy)

    def DeletionPolicy(self, deletion_policy: Union[str, AnyFn]):
        return self.__set_common_property(self.DeletionPolicy.__name__, deletion_policy)

    def DependsOn(self, *depends_on: Union[str, AnyFn]):
        return self.__set_common_property(self.DependsOn.__name__, list(depends_on))

    def Metadata(self, metadata: Metadata):
        return self.__set_common_property(self.Metadata.__name__, metadata)

    def UpdatePolicy(self, update_policy: UpdatePolicy):
        return self.__set_common_property(self.UpdatePolicy.__name__, update_policy)

    def UpdateReplacePolicy(self, update_replace_policy: Union[str, AnyFn]):
        return self.__set_common_property(self.UpdateReplacePolicy.__name__, update_replace_policy)

    def __to_dict__(self, **kwargs):
        return super(Resource, self).__to_dict__(id=self.__id)
