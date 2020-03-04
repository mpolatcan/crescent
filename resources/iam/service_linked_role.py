from resources.shared.base_cf_resource_model import BaseCloudFormationResourceModel


class ServiceLinkedRole(BaseCloudFormationResourceModel):
    __TYPE = "AWS::IAM::ServiceLinkedRole"
    __PROPERTY_AWS_SERVICE_NAME = "AWSServiceName"
    __PROPERTY_CUSTOM_SUFFIX = "CustomSuffix"
    __PROPERTY_DESCRIPTION = "Description"

    def __init__(self):
        super(ServiceLinkedRole, self).__init__(type=self.__TYPE)

    def aws_service_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_AWS_SERVICE_NAME, value)

    def custom_suffix(self, value: str):
        return self._add_property_field(self.__PROPERTY_CUSTOM_SUFFIX, value)

    def description(self, value: str):
        return self._add_property_field(self.__PROPERTY_DESCRIPTION, value)