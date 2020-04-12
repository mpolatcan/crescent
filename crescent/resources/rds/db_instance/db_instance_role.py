from crescent.core import Model
from crescent.functions import AnyFn
from .constants import ModelRequiredProperties
from typing import Union


class DBInstanceRole(Model):
    def __init__(self):
        super(DBInstanceRole, self).__init__(required_properties=ModelRequiredProperties.DB_INSTANCE_ROLE)

    def FeatureName(self, feature_name: Union[str, AnyFn]):
        return self._set_field(self.FeatureName.__name__, feature_name)

    def RoleArn(self, role_arn: Union[str, AnyFn]):
        return self._set_field(self.RoleArn.__name__, role_arn)
