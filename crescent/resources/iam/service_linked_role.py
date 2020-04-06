from crescent.core import Resource
from .constants import ResourceRequiredProperties


class ServiceLinkedRole(Resource):
    __TYPE = "AWS::IAM::ServiceLinkedRole"

    def __init__(self, id: str):
        super(ServiceLinkedRole, self).__init__(
            id=id,
            type=self.__TYPE,
            min_length={self.AWSServiceName.__name__: 1,
                        self.CustomSuffix.__name__: 1},
            max_length={self.AWSServiceName.__name__: 128,
                        self.CustomSuffix.__name__: 64,
                        self.Description.__name__: 1000},
            pattern={self.AWSServiceName.__name__: r"[\w+=,.@-]+",
                     self.CustomSuffix.__name__: r"[\w+=,.@-]+",
                     self.Description.__name__: r"[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*"},
            required_properties=ResourceRequiredProperties.SERVICE_LINKED_ROLE
        )

    def AWSServiceName(self, aws_service_name: str):
        return self._set_property(self.AWSServiceName.__name__, aws_service_name)

    def CustomSuffix(self, custom_suffix: str):
        return self._set_property(self.CustomSuffix.__name__, custom_suffix)

    def Description(self, description: str):
        return self._set_property(self.Description.__name__, description)