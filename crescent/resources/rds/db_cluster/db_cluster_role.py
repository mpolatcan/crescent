from crescent.core import Model
from crescent.functions import AnyFn
from crescent.resources.iam import RoleArn
from .constants import ModelRequiredProperties
from typing import Union


class DBClusterRole(Model):
    def __init__(self):
        super(DBClusterRole, self).__init__(
            pattern={self.RoleArn.__name__: r"arn:.*"},
            required_properties=ModelRequiredProperties.DB_CLUSTER_ROLE
        )

    def FeatureName(self, feature_name: Union[str, AnyFn]):
        return self._set_field(self.FeatureName.__name__, feature_name)

    def RoleArn(self, role_arn: RoleArn):
        return self._set_field(self.RoleArn.__name__, role_arn)
