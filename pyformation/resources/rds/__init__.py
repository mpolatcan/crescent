from .db_cluster import DBCluster, DBClusterRole, ScalingConfiguration
from .db_cluster_pg import DBClusterParameterGroup
from .db_instance import DBInstance, DBInstanceRole, ProcessorFeature
from .db_pg import DBParameterGroup
from .db_security_group import DBSecurityGroup, Ingress
from .db_security_group_ingress import DBSecurityGroupIngress
from .db_subnet_group import DBSubnetGroup
from .event_subscription import EventSubscription
from .option_group import OptionGroup, OptionConfiguration, OptionSetting


class RdsFactory:
    @staticmethod
    def DBCluster(id: str):
        return DBCluster(id)

    @staticmethod
    def DBClusterRole():
        return DBClusterRole()

    @staticmethod
    def ScalingConfiguration():
        return ScalingConfiguration()

    @staticmethod
    def DBClusterParameterGroup(id: str):
        return DBClusterParameterGroup(id)

    @staticmethod
    def DBInstance(id: str):
        return DBInstance(id)

    @staticmethod
    def DBInstanceRole():
        return DBInstanceRole()

    @staticmethod
    def ProcessorFeature():
        return ProcessorFeature()

    @staticmethod
    def DBParameterGroup(id: str):
        return DBParameterGroup(id)

    @staticmethod
    def DBSecurityGroup(id: str):
        return DBSecurityGroup(id)

    @staticmethod
    def Ingress():
        return Ingress()

    @staticmethod
    def DBSecurityGroupIngress(id: str):
        return DBSecurityGroupIngress(id)

    @staticmethod
    def DBSubnetGroup(id: str):
        return DBSubnetGroup(id)

    @staticmethod
    def EventSubscription(id: str):
        return EventSubscription(id)

    @staticmethod
    def OptionGroup(id: str):
        return OptionGroup(id)

    @staticmethod
    def OptionConfiguration():
        return OptionConfiguration()

    @staticmethod
    def OptionSetting():
        return OptionSetting()


__all__ = [
    "RdsFactory"
]
