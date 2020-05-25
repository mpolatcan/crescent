from crescent.core import Arn


class RdsArn(Arn):
    __SERVICE_RDS = "rds"

    def __new__(cls, suffix: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(RdsArn, cls).__new__(
            cls, suffix=suffix, service=cls.__SERVICE_RDS, region=region, account_id=account_id, partition=partition
        )


# --------------------------


class ClusterArn(RdsArn):
    __CLUSTER_ARN_SUFFIX = "cluster:{}"

    def __new__(cls, cluster_instance_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(ClusterArn, cls).__new__(cls,
                                              suffix=cls.__CLUSTER_ARN_SUFFIX.format(cluster_instance_name),
                                              region=region,
                                              account_id=account_id,
                                              partition=partition)


# --------------------------


class ClusterEndpointArn(RdsArn):
    __CLUSTER_ENDPOINT_ARN_SUFFIX = "cluster-endpoint:{}"

    def __new__(cls, cluster_endpoint: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(ClusterEndpointArn, cls).__new__(cls,
                                                      suffix=cls.__CLUSTER_ENDPOINT_ARN_SUFFIX.format(cluster_endpoint),
                                                      region=region,
                                                      account_id=account_id,
                                                      partition=partition)


# ---------------------------


class ClusterParameterGroupArn(RdsArn):
    __CLUSTER_PARAMETER_GROUP_ARN_SUFFIX = "cluster-pg:{}"

    def __new__(cls, cluster_pg_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(ClusterParameterGroupArn, cls).__new__(cls,
                                                            suffix=cls.__CLUSTER_PARAMETER_GROUP_ARN_SUFFIX.format(cluster_pg_name),
                                                            region=region,
                                                            account_id=account_id,
                                                            partition=partition)


# -----------------------------


class ClusterSnapshotArn(RdsArn):
    __CLUSTER_SNAPSHOT_ARN_SUFFIX = "cluster-snapshot:{}"

    def __new__(cls, cluster_snapshot_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(ClusterSnapshotArn, cls).__new__(cls,
                                                      suffix=cls.__CLUSTER_SNAPSHOT_ARN_SUFFIX.format(cluster_snapshot_name),
                                                      region=region,
                                                      account_id=account_id,
                                                      partition=partition)


# ------------------------------


class DBArn(RdsArn):
    __DB_ARN_SUFFIX = "db:{}"

    def __new__(cls, db_instance_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(DBArn, cls).__new__(cls,
                                         suffix=cls.__DB_ARN_SUFFIX.format(db_instance_name),
                                         region=region,
                                         account_id=account_id,
                                         partition=partition)


# -------------------------------


class EventSubscriptionArn(RdsArn):
    __EVENT_SUBSCRIPTION_ARN_SUFFIX = "es:{}"

    def __new__(cls, subscription_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(EventSubscriptionArn, cls).__new__(cls,
                                                        suffix=cls.__EVENT_SUBSCRIPTION_ARN_SUFFIX.format(subscription_name),
                                                        region=region,
                                                        account_id=account_id,
                                                        partition=partition)


# -------------------------------


class OptionGroupArn(RdsArn):
    __OPTION_GROUP_ARN = "og:{}"

    def __new__(cls, option_group_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(OptionGroupArn, cls).__new__(cls,
                                                  suffix=cls.__OPTION_GROUP_ARN.format(option_group_name),
                                                  region=region,
                                                  account_id=account_id,
                                                  partition=partition)


# --------------------------------


class ParameterGroupArn(RdsArn):
    __PARAMETER_GROUP_ARN_SUFFIX = "pg:{}"

    def __new__(cls, parameter_group_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(ParameterGroupArn, cls).__new__(cls,
                                                     suffix=cls.__PARAMETER_GROUP_ARN_SUFFIX.format(parameter_group_name),
                                                     region=region,
                                                     account_id=account_id,
                                                     partition=partition)


# ---------------------------------


class ProxyArn(RdsArn):
    __PROXY_ARN_SUFFIX = "db-proxy:{}"

    def __new__(cls, db_proxy_id: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(ProxyArn, cls).__new__(cls,
                                            suffix=cls.__PROXY_ARN_SUFFIX.format(db_proxy_id),
                                            region=region,
                                            account_id=account_id,
                                            partition=partition)


# ---------------------------------


class ReservedInstanceArn(RdsArn):
    __RESERVED_INSTANCE_ARN_SUFFIX = "ri:{}"

    def __new__(cls, reserved_db_instance_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(ReservedInstanceArn, cls).__new__(cls,
                                                       suffix=cls.__RESERVED_INSTANCE_ARN_SUFFIX.format(reserved_db_instance_name),
                                                       region=region,
                                                       account_id=account_id,
                                                       partition=partition)


# ---------------------------------


class SecurityGroupArn(RdsArn):
    __SECURITY_GROUP_ARN_SUFFIX = "secgrp:{}"

    def __new__(cls, security_group_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(SecurityGroupArn, cls).__new__(cls,
                                                    suffix=cls.__SECURITY_GROUP_ARN_SUFFIX.format(security_group_name),
                                                    region=region,
                                                    account_id=account_id,
                                                    partition=partition)


# ---------------------------------


class SnapshotArn(RdsArn):
    __SNAPSHOT_ARN_SUFFIX = "snapshot:{}"

    def __new__(cls, snapshot_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(SnapshotArn, cls).__new__(cls,
                                               suffix=cls.__SNAPSHOT_ARN_SUFFIX.format(snapshot_name),
                                               region=region,
                                               account_id=account_id,
                                               partition=partition)


# ---------------------------------


class SubnetGroupArn(RdsArn):
    __SUBNET_GROUP_ARN_SUFFIX = "subgrp:{}"

    def __new__(cls, subnet_group_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(SubnetGroupArn, cls).__new__(cls,
                                                  suffix=cls.__SUBNET_GROUP_ARN_SUFFIX.format(subnet_group_name),
                                                  region=region,
                                                  account_id=account_id,
                                                  partition=partition)


# ---------------------------------


class TargetArn(RdsArn):
    __TARGET_ARN_SUFFIX = "target:{}"

    def __new__(cls, target_id: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(TargetArn, cls).__new__(cls,
                                             suffix=cls.__TARGET_ARN_SUFFIX.format(target_id),
                                             region=region,
                                             account_id=account_id,
                                             partition=partition)


# ---------------------------------


class TargetGroupArn(RdsArn):
    __TARGET_GROUP_ARN_SUFFIX = "target-group:{}"

    def __new__(cls, target_group_id: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(TargetGroupArn, cls).__new__(cls,
                                                  suffix=cls.__TARGET_GROUP_ARN_SUFFIX.format(target_group_id),
                                                  region=region,
                                                  account_id=account_id,
                                                  partition=partition)

# ---------------------------------


class ArnFactory:
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
