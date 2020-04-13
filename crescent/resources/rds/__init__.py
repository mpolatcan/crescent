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
from .constants import EngineVersion, EngineFamily


class Rds:
    class Arn:
        @staticmethod
        def ClusterArn(cluster_instance_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
            return ClusterArn(cluster_instance_name=cluster_instance_name,
                              partition=partition,
                              region=region,
                              account_id=account_id)

        @staticmethod
        def ClusterEndpointArn(cluster_endpoint: str, partition: str = "aws", region: str = "", account_id: str = ""):
            return ClusterEndpointArn(cluster_endpoint=cluster_endpoint,
                                      partition=partition,
                                      region=region,
                                      account_id=account_id)

        @staticmethod
        def ClusterParameterGroupArn(cluster_pg_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
            return ClusterParameterGroupArn(cluster_pg_name=cluster_pg_name,
                                            partition=partition,
                                            region=region,
                                            account_id=account_id)

        @staticmethod
        def ClusterSnapshotArn(cluster_snapshot_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
            return ClusterSnapshotArn(cluster_snapshot_name=cluster_snapshot_name,
                                      partition=partition,
                                      region=region,
                                      account_id=account_id)

        @staticmethod
        def DBArn(db_instance_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
            return DBArn(db_instance_name=db_instance_name,
                         partition=partition,
                         region=region,
                         account_id=account_id)

        @staticmethod
        def EventSubscriptionArn(subscription_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
            return EventSubscriptionArn(subscription_name=subscription_name,
                                        partition=partition,
                                        region=region,
                                        account_id=account_id)

        @staticmethod
        def OptionGroupArn(option_group_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
            return OptionGroupArn(option_group_name=option_group_name,
                                  partition=partition,
                                  region=region,
                                  account_id=account_id)

        @staticmethod
        def ParameterGroupArn(parameter_group_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
            return ParameterGroupArn(parameter_group_name=parameter_group_name,
                                     partition=partition,
                                     region=region,
                                     account_id=account_id)

        @staticmethod
        def ProxyArn(db_proxy_id: str, partition: str = "aws", region: str = "", account_id: str = ""):
            return ProxyArn(db_proxy_id=db_proxy_id,
                            partition=partition,
                            region=region,
                            account_id=account_id)

        @staticmethod
        def ReservedInstanceArn(reserved_db_instance_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
            return ReservedInstanceArn(reserved_db_instance_name=reserved_db_instance_name,
                                       partition=partition,
                                       region=region,
                                       account_id=account_id)

        @staticmethod
        def SecurityGroupArn(security_group_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
            return SecurityGroupArn(security_group_name=security_group_name,
                                    partition=partition,
                                    region=region,
                                    account_id=account_id)

        @staticmethod
        def SnapshotArn(snapshot_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
            return SnapshotArn(snapshot_name=snapshot_name,
                               partition=partition,
                               region=region,
                               account_id=account_id)

        @staticmethod
        def SubnetGroupArn(subnet_group_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
            return SubnetGroupArn(subnet_group_name=subnet_group_name,
                                  partition=partition,
                                  region=region,
                                  account_id=account_id)

        @staticmethod
        def TargetArn(target_id: str, partition: str = "aws", region: str = "", account_id: str = ""):
            return TargetArn(target_id=target_id,
                             partition=partition,
                             region=region,
                             account_id=account_id)

        @staticmethod
        def TargetGroupArn(target_group_id: str, partition: str = "aws", region: str = "", account_id: str = ""):
            return TargetGroupArn(target_group_id=target_group_id,
                                  partition=partition,
                                  region=region,
                                  account_id=account_id)

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


__all__ = [
   "Rds"
]
