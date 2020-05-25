from .arn import ArnFactory
from .db_cluster import DBClusterFactory
from .db_cluster_pg import DBClusterParameterGroupFactory
from .db_instance import DBInstanceFactory
from .db_pg import DBParameterGroupFactory
from .db_security_group import DBSecurityGroupFactory
from .db_security_group_ingress import DBSecurityGroupIngressFactory
from .db_subnet_group import DBSubnetGroupFactory
from .event_subscription import EventSubscriptionFactory
from .option_group import OptionGroupFactory
from .constants import *


class Rds:
    Arn = ArnFactory
    DBCluster = DBClusterFactory
    DBClusterParameterGroup = DBClusterParameterGroupFactory
    DBInstance = DBInstanceFactory
    DBParameterGroup = DBClusterParameterGroupFactory
    DBSecurityGroup = DBSecurityGroupFactory
    DBSecurityGroupIngress = DBSecurityGroupIngressFactory
    DBSubnetGroup = DBSubnetGroupFactory
    EventSubscription = EventSubscriptionFactory
    OptionGroup = OptionGroupFactory


__all__ = ["Rds"]
