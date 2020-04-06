from crescent.core import Resource
from .constants import ResourceRequiredProperties


class InstanceProfile(Resource):
    __TYPE = "AWS::IAM::InstanceProfile"

    def __init__(self, id: str):
        super(InstanceProfile, self).__init__(
            id=id,
            type=self.__TYPE,
            min_length={self.InstanceProfileName.__name__: 1,
                        self.Path.__name__: 1},
            max_length={self.InstanceProfileName.__name__: 128,
                        self.Path.__name__: 512},
            pattern={self.InstanceProfileName.__name__: r"[\w+=,.@-]+",
                     self.Path.__name__: r"(\u002F)|(\u002F[\u0021-\u007F]+\u002F)"},
            required_properties=ResourceRequiredProperties.INSTANCE_PROFILE
        )

    def InstanceProfileName(self, instance_profile_name: str):
        return self._set_property(self.InstanceProfileName.__name__, instance_profile_name)

    def Path(self, path: str):
        return self._set_property(self.Path.__name__, path)

    def Roles(self, *roles: str):
        return self._set_property(self.Roles.__name__, list(roles))
