from crescent.core import Resource, Tag
from crescent.functions import AnyFn
from .constants import AllowedValues, ResourceRequiredProperties
from typing import Union


class DBClusterParameterGroup(Resource):
    __TYPE = "AWS::RDS::DBClusterParameterGroup"

    def __init__(self, id: str):
        super(DBClusterParameterGroup, self).__init__(
            id=id,
            type=self.__TYPE,
            allowed_values={self.Family.__name__: AllowedValues.FAMILY},
            required_properties=ResourceRequiredProperties.DB_CLUSTER_PARAMETER_GROUP
        )

    def Description(self, description: Union[str, AnyFn]):
        return self._set_property(self.Description.__name__, description)

    def Family(self, family: Union[str, AnyFn]):
        return self._set_property(self.Family.__name__, family)

    def Parameters(self, parameters: Union[dict, AnyFn]):
        return self._set_property(self.Parameters.__name__, parameters)

    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))
