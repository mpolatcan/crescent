from crescent.core import Arn


class RdsArn(Arn):
    __SERVICE_RDS = "rds"

    def __new__(cls, suffix: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(RdsArn, cls).__new__(
            cls, suffix=suffix, service=cls.__SERVICE_RDS, partition=partition, region=region, account_id=account_id
        )


# --------------------------


class ClusterArn(RdsArn):
    __CLUSTER_ARN_SUFFIX = "cluster:{}"

    def __new__(cls, cluster_instance_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(ClusterArn, cls).__new__(cls,
                                              suffix=cls.__CLUSTER_ARN_SUFFIX.format(cluster_instance_name),
                                              partition=partition,
                                              region=region,
                                              account_id=account_id)


# --------------------------


class ClusterEndpointArn(RdsArn):
    __CLUSTER_ENDPOINT_ARN_SUFFIX = "cluster-endpoint:{}"

    def __new__(cls, cluster_endpoint: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(ClusterEndpointArn, cls).__new__(cls,
                                                      suffix=cls.__CLUSTER_ENDPOINT_ARN_SUFFIX.format(cluster_endpoint),
                                                      partition=partition,
                                                      region=region,
                                                      account_id=account_id)


# ---------------------------


class ClusterParameterGroupArn(RdsArn):
    __CLUSTER_PARAMETER_GROUP_ARN_SUFFIX = "cluster-pg:{}"

    def __new__(cls, cluster_pg_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(ClusterParameterGroupArn, cls).__new__(cls,
                                                            suffix=cls.__CLUSTER_PARAMETER_GROUP_ARN_SUFFIX.format(cluster_pg_name),
                                                            partition=partition,
                                                            region=region,
                                                            account_id=account_id)


# -----------------------------


class ClusterSnapshotArn(RdsArn):
    __CLUSTER_SNAPSHOT_ARN_SUFFIX = "cluster-snapshot:{}"

    def __new__(cls, cluster_snapshot_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(ClusterSnapshotArn, cls).__new__(cls,
                                                      suffix=cls.__CLUSTER_SNAPSHOT_ARN_SUFFIX.format(cluster_snapshot_name),
                                                      partition=partition,
                                                      region=region,
                                                      account_id=account_id)


# ------------------------------


class DBArn(RdsArn):
    __DB_ARN_SUFFIX = "db:{}"

    def __new__(cls, db_instance_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(DBArn, cls).__new__(cls,
                                         suffix=cls.__DB_ARN_SUFFIX.format(db_instance_name),
                                         partition=partition,
                                         region=region,
                                         account_id=account_id)


# -------------------------------


class EventSubscriptionArn(RdsArn):
    __EVENT_SUBSCRIPTION_ARN_SUFFIX = "es:{}"

    def __new__(cls, subscription_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(EventSubscriptionArn, cls).__new__(cls,
                                                        suffix=cls.__EVENT_SUBSCRIPTION_ARN_SUFFIX.format(subscription_name),
                                                        partition=partition,
                                                        region=region,
                                                        account_id=account_id)


# -------------------------------


class OptionGroupArn(RdsArn):
    __OPTION_GROUP_ARN = "og:{}"

    def __new__(cls, option_group_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(OptionGroupArn, cls).__new__(cls,
                                                  suffix=cls.__OPTION_GROUP_ARN.format(option_group_name),
                                                  partition=partition,
                                                  region=region,
                                                  account_id=account_id)


# --------------------------------


class ParameterGroupArn(RdsArn):
    __PARAMETER_GROUP_ARN_SUFFIX = "pg:{}"

    def __new__(cls, parameter_group_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(ParameterGroupArn, cls).__new__(cls,
                                                     suffix=cls.__PARAMETER_GROUP_ARN_SUFFIX.format(parameter_group_name),
                                                     partition=partition,
                                                     region=region,
                                                     account_id=account_id)


# ---------------------------------


class ProxyArn(RdsArn):
    __PROXY_ARN_SUFFIX = "db-proxy:{}"

    def __new__(cls, db_proxy_id: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(ProxyArn, cls).__new__(cls,
                                            suffix=cls.__PROXY_ARN_SUFFIX.format(db_proxy_id),
                                            partition=partition,
                                            region=region,
                                            account_id=account_id)


# ---------------------------------


class ReservedInstanceArn(RdsArn):
    __RESERVED_INSTANCE_ARN_SUFFIX = "ri:{}"

    def __new__(cls, reserved_db_instance_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(ReservedInstanceArn, cls).__new__(cls,
                                                       suffix=cls.__RESERVED_INSTANCE_ARN_SUFFIX.format(reserved_db_instance_name),
                                                       partition=partition,
                                                       region=region,
                                                       account_id=account_id)


# ---------------------------------


class SecurityGroupArn(RdsArn):
    __SECURITY_GROUP_ARN_SUFFIX = "secgrp:{}"

    def __new__(cls, security_group_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(SecurityGroupArn, cls).__new__(cls,
                                                    suffix=cls.__SECURITY_GROUP_ARN_SUFFIX.format(security_group_name),
                                                    partition=partition,
                                                    region=region,
                                                    account_id=account_id)


# ---------------------------------


class SnapshotArn(RdsArn):
    __SNAPSHOT_ARN_SUFFIX = "snapshot:{}"

    def __new__(cls, snapshot_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(SnapshotArn, cls).__new__(cls,
                                               suffix=cls.__SNAPSHOT_ARN_SUFFIX.format(snapshot_name),
                                               partition=partition,
                                               region=region,
                                               account_id=account_id)


# ---------------------------------


class SubnetGroupArn(RdsArn):
    __SUBNET_GROUP_ARN_SUFFIX = "subgrp:{}"

    def __new__(cls, subnet_group_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(SubnetGroupArn, cls).__new__(cls,
                                                  suffix=cls.__SUBNET_GROUP_ARN_SUFFIX.format(subnet_group_name),
                                                  partition=partition,
                                                  region=region,
                                                  account_id=account_id)


# ---------------------------------


class TargetArn(RdsArn):
    __TARGET_ARN_SUFFIX = "target:{}"

    def __new__(cls, target_id: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(TargetArn, cls).__new__(cls,
                                             suffix=cls.__TARGET_ARN_SUFFIX.format(target_id),
                                             partition=partition,
                                             region=region,
                                             account_id=account_id)


# ---------------------------------


class TargetGroupArn(RdsArn):
    __TARGET_GROUP_ARN_SUFFIX = "target-group:{}"

    def __new__(cls, target_group_id: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(TargetGroupArn, cls).__new__(cls,
                                                  suffix=cls.__TARGET_GROUP_ARN_SUFFIX.format(target_group_id),
                                                  partition=partition,
                                                  region=region,
                                                  account_id=account_id)
