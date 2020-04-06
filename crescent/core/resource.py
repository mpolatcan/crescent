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
from .model import Model
from .constants import get_values
from .resource_attrs import CreationPolicy, DeletionPolicy, UpdatePolicy, UpdateReplacePolicy


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
        self.__resource_def = self.__get_field__(self.__id)
        self._properties = self.__resource_def[self.__KEY_PROPERTIES]

    def _set_property(self, property, value):
        self._properties[property] = value

        return self

    def __get_properties__(self):
        return self._properties

    def CreationPolicy(self, creation_policy: CreationPolicy):
        self.__resource_def[self.CreationPolicy.__name__] = creation_policy
        return self

    def DeletionPolicy(self, deletion_policy: str):
        self.__resource_def[self.DeletionPolicy.__name__] = deletion_policy
        return self

    def DependsOn(self, *depends_on: str):
        self.__resource_def[self.DependsOn.__name__] = list(depends_on)
        return self

    # FIXME Metadata section will be fixed
    def Metadata(self, **metadatas: dict):
        self.__resource_def[self.Metadata.__name__] = metadatas
        return self

    def UpdatePolicy(self, update_policy: UpdatePolicy):
        self.__resource_def[self.UpdatePolicy.__name__] = update_policy
        return self

    def UpdateReplacePolicy(self, update_replace_policy: str):
        self.__resource_def[self.UpdateReplacePolicy.__name__] = update_replace_policy
        return self
    
    def __to_dict__(self, **kwargs):
        return super(Resource, self).__to_dict__(id=self.__id)
