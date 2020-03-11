from pyformation.resources.shared import BaseModel


class DBClusterRole(BaseModel):
    __PROPERTY_FEATURE_NAME = "FeatureName"
    __PROPERTY_ROLE_ARN = "RoleArn"

    def feature_name(self, value: str):
        return self._add_field(self.__PROPERTY_FEATURE_NAME, value)

    def role_arn(self, value: str):
        return self._add_field(self.__PROPERTY_ROLE_ARN, value)
