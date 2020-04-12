from crescent.core import Resource
from crescent.functions import AnyFn
from .constants import AllowedValues, ResourceRequiredProperties
from typing import Union


class AccessKey(Resource):
    __TYPE = "AWS::IAM::AccessKey"

    def __init__(self, id: str):
        super(AccessKey, self).__init__(
            id=id,
            type=self.__TYPE,
            min_length={self.Username.__name__: 1},
            max_length={self.Username.__name__: 128},
            pattern={self.Username.__name__: r"[\w+=,.@-]+"},
            allowed_values={self.Status.__name__: AllowedValues.STATUS},
            required_properties=ResourceRequiredProperties.ACCESS_KEY
        )

    def Serial(self, serial: Union[int, AnyFn]):
        return self._set_property(self.Serial.__name__, serial)

    def Status(self, status: Union[str, AnyFn]):
        return self._set_property(self.Status.__name__, status)

    def Username(self, username: Union[str, AnyFn]):
        return self._set_property(self.Username.__name__, username)
