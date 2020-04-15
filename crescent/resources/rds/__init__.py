from .arn import *
from .db_cluster import *
from .db_cluster_pg import *
from .db_instance import *
from .db_pg import *
from .db_security_group import *
from .db_security_group_ingress import *
from .db_subnet_group import *
from .event_subscription import *
from .option_group import *
from .constants import *


class Rds:
    class Arn:
        @staticmethod
        def ClusterArn(cluster_instance_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
            return ClusterArn(cluster_instance_name=cluster_instance_name, region=region,
                              account_id=account_id, partition=partition)

        @staticmethod
        def ClusterEndpointArn(cluster_endpoint: str, region: str = "", account_id: str = "", partition: str = "aws"):
            return ClusterEndpointArn(cluster_endpoint=cluster_endpoint, region=region,
                                      account_id=account_id, partition=partition)

        @staticmethod
        def ClusterParameterGroupArn(cluster_pg_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
            return ClusterParameterGroupArn(cluster_pg_name=cluster_pg_name, region=region,
                                            account_id=account_id, partition=partition)

        @staticmethod
        def ClusterSnapshotArn(cluster_snapshot_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
            return ClusterSnapshotArn(cluster_snapshot_name=cluster_snapshot_name, region=region,
                                      account_id=account_id, partition=partition)

        @staticmethod
        def DBArn(db_instance_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
            return DBArn(db_instance_name=db_instance_name, region=region, account_id=account_id, partition=partition)

        @staticmethod
        def EventSubscriptionArn(subscription_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
            return EventSubscriptionArn(subscription_name=subscription_name,region=region,
                                        account_id=account_id, partition=partition)

        @staticmethod
        def OptionGroupArn(option_group_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
            return OptionGroupArn(option_group_name=option_group_name, region=region,
                                  account_id=account_id, partition=partition)

        @staticmethod
        def ParameterGroupArn(parameter_group_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
            return ParameterGroupArn(parameter_group_name=parameter_group_name, region=region,
                                     account_id=account_id, partition=partition)

        @staticmethod
        def ProxyArn(db_proxy_id: str, region: str = "", account_id: str = "", partition: str = "aws"):
            return ProxyArn(db_proxy_id=db_proxy_id, region=region, account_id=account_id, partition=partition)

        @staticmethod
        def ReservedInstanceArn(reserved_db_instance_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
            return ReservedInstanceArn(reserved_db_instance_name=reserved_db_instance_name, region=region,
                                       account_id=account_id, partition=partition)

        @staticmethod
        def SecurityGroupArn(security_group_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
            return SecurityGroupArn(security_group_name=security_group_name, region=region,
                                    account_id=account_id, partition=partition)

        @staticmethod
        def SnapshotArn(snapshot_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
            return SnapshotArn(snapshot_name=snapshot_name, region=region, account_id=account_id, partition=partition)

        @staticmethod
        def SubnetGroupArn(subnet_group_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
            return SubnetGroupArn(subnet_group_name=subnet_group_name,  region=region,
                                  account_id=account_id, partition=partition)

        @staticmethod
        def TargetArn(target_id: str, region: str = "", account_id: str = "", partition: str = "aws"):
            return TargetArn(target_id=target_id, region=region, account_id=account_id, partition=partition)

        @staticmethod
        def TargetGroupArn(target_group_id: str, region: str = "", account_id: str = "", partition: str = "aws"):
            return TargetGroupArn(target_group_id=target_group_id, region=region,
                                  account_id=account_id, partition=partition)

    class DBCluster:
        Engine = DBClusterEngine
        EngineVersion = DBClusterEngineVersion
        EngineMode = EngineMode
        RestoreType = RestoreType
        Capacity = Capacity

        @staticmethod
        def Create(id: str): return DBCluster(id)

        @staticmethod
        def DBClusterRole(): return DBClusterRole()

        @staticmethod
        def ScalingConfiguration(): return ScalingConfiguration()

    class DBClusterParameterGroup:
        EngineFamily = DBClusterParameterGroupEngineFamily

        @staticmethod
        def Create(id: str): return DBClusterParameterGroup(id)

    class DBInstance:
        Engine = DBInstanceEngine
        EngineVersion = EngineVersion
        DBInstanceClass = DBInstanceClass
        MonitoringInterval = MonitoringInterval
        StorageType = StorageType

        @staticmethod
        def Create(id: str): return DBInstance(id)

        @staticmethod
        def DBInstanceRole(): return DBInstanceRole()

        @staticmethod
        def ProcessorFeature(): return ProcessorFeature()

    class DBParameterGroup:
        EngineFamily = EngineFamily

        @staticmethod
        def Create(id: str): return DBParameterGroup(id)

    class DBSecurityGroup:
        @staticmethod
        def Create(id: str): return DBSecurityGroup(id)

        @staticmethod
        def Ingress(): return Ingress()

    class DBSecurityGroupIngress:
        @staticmethod
        def Create(id: str): return DBSecurityGroupIngress(id)

    class DBSubnetGroup:
        @staticmethod
        def Create(id: str): return DBSubnetGroup(id)

    class OptionGroup:
        @staticmethod
        def Create(id: str): return OptionGroup(id)

        @staticmethod
        def OptionConfiguration(): return OptionConfiguration()

        @staticmethod
        def OptionSetting(): return OptionSetting()

    class EventSubscription:
        EventCategories = EventCategories
        SourceType = SourceType

        @staticmethod
        def Create(id: str): return EventSubscription(id)


__all__ = ["Rds"]
