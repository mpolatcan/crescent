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
        self._set_field(id, {
            self.__KEY_TYPE: type,
            self.__KEY_PROPERTIES: {}
        })
        self._properties = self._get_field(id)[self.__KEY_PROPERTIES]

    def _set_property(self, property, value):
        self._properties[property] = value

        return self

    def __get_properties__(self):
        return self._properties

    @Validator.validate(type=CreationPolicy)
    def CreationPolicy(self, creation_policy: CreationPolicy):
        return self._set_field(self.CreationPolicy.__name__, creation_policy.__to_dict__())

    @Validator.validate(type=str, allowed_values=[DeletionPolicy.DELETE,
                                                  DeletionPolicy.RETAIN,
                                                  DeletionPolicy.SNAPSHOT])
    def DeletionPolicy(self, deletion_policy: str):
        return self._set_field(self.DeletionPolicy.__name__, deletion_policy)

    @Validator.validate(type=str)
    def DependsOn(self, *depends_on: str):
        return self._set_field(self.DependsOn.__name__, list(depends_on))

    def Metadata(self, *metadatas):
        if self._get_field(self.Metadata.__name__) is None:
            self._set_field(self.Metadata.__name__, {})

        for metadata in list(metadatas):
            self._get_field(self.Metadata.__name__).update(metadata)

        return self

    @Validator.validate(type=UpdatePolicy)
    def UpdatePolicy(self, update_policy: UpdatePolicy):
        return self._set_field(self.UpdatePolicy.__name__, update_policy.__to_dict__())

    @Validator.validate(type=str, allowed_values=[UpdateReplacePolicy.DELETE,
                                                  UpdateReplacePolicy.RETAIN,
                                                  UpdateReplacePolicy.SNAPSHOT])
    def UpdateReplacePolicy(self, update_replace_policy: str):
        return self._set_field(self.UpdateReplacePolicy.__name__, update_replace_policy)
