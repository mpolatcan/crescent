from crescent.resources.rds.arn import *
from .action import Action, AccessLevelAllActions
from typing import Union


class RdsAction(Action):
    __SERVICE_RDS = "rds"

    def __init__(self, action_name, **definable_resources):
        super(RdsAction, self).__init__(self.__SERVICE_RDS, action_name, **definable_resources)

    def Cluster(self, cluster: Union[str, ClusterArn]):
        return self._set_resource(self.Cluster.__name__, cluster)

    def ClusterEndpoint(self, cluster_endpoint: Union[str, ClusterEndpointArn]):
        return self._set_resource(self.ClusterEndpoint.__name__, cluster_endpoint)

    def ClusterParameterGroup(self, cluster_pg: Union[str, ClusterParameterGroupArn]):
        return self._set_resource(self.ClusterParameterGroup.__name__, cluster_pg)

    def ClusterSnapshot(self, cluster_snapshot: Union[str, ClusterSnapshotArn]):
        return self._set_resource(self.ClusterSnapshot.__name__, cluster_snapshot)

    def DBInstance(self, db_instance: Union[str, DBArn]):
        return self._set_resource(self.DBInstance.__name__, db_instance)

    def EventSubscription(self, event_subscription: Union[str, EventSubscriptionArn]):
        return self._set_resource(self.EventSubscription.__name__, event_subscription)

    def OptionGroup(self, option_group: Union[str, OptionGroupArn]):
        return self._set_resource(self.OptionGroup.__name__, option_group)

    def ParameterGroup(self, parameter_group: Union[str, ParameterGroupArn]):
        return self._set_resource(self.ParameterGroup.__name__, parameter_group)

    def Proxy(self, proxy: Union[str, ProxyArn]):
        return self._set_resource(self.Proxy.__name__, proxy)

    def ReservedInstance(self, reserved_instance: Union[str, ReservedInstanceArn]):
        return self._set_resource(self.ReservedInstance.__name__, reserved_instance)

    def SecurityGroup(self, security_group: Union[str, SecurityGroupArn]):
        return self._set_resource(self.SecurityGroup.__name__, security_group)

    def Snapshot(self, snapshot: Union[str, SnapshotArn]):
        return self._set_resource(self.Snapshot.__name__, snapshot)

    def SubnetGroup(self, subnet_group: Union[str, SubnetGroupArn]):
        return self._set_resource(self.SubnetGroup.__name__, subnet_group)

    def Target(self, target: Union[str, TargetArn]):
        return self._set_resource(self.Target.__name__, target)

    def TargetGroup(self, target_group: Union[str, TargetGroupArn]):
        return self._set_resource(self.TargetGroup.__name__, target_group)


# ---------------------------------------------


class RdsAccessLevellAllActions(AccessLevelAllActions):
    def __init__(self, access_level):
        super(RdsAccessLevellAllActions, self).__init__(access_level)

    def Cluster(self, cluster: Union[str, ClusterArn]):
        return self._set_all_actions_resources(self.Cluster.__name__, cluster)

    def ClusterEndpoint(self, cluster_endpoint: Union[str, ClusterEndpointArn]):
        return self._set_all_actions_resources(self.ClusterEndpoint.__name__, cluster_endpoint)

    def ClusterParameterGroup(self, cluster_pg: Union[str, ClusterParameterGroupArn]):
        return self._set_all_actions_resources(self.ClusterParameterGroup.__name__, cluster_pg)

    def ClusterSnapshot(self, cluster_snapshot: Union[str, ClusterSnapshotArn]):
        return self._set_all_actions_resources(self.ClusterSnapshot.__name__, cluster_snapshot)

    def DBInstance(self, db_instance: Union[str, DBArn]):
        return self._set_all_actions_resources(self.DBInstance.__name__, db_instance)

    def EventSubscription(self, event_subscription: Union[str, EventSubscriptionArn]):
        return self._set_all_actions_resources(self.EventSubscription.__name__, event_subscription)

    def OptionGroup(self, option_group: Union[str, OptionGroupArn]):
        return self._set_all_actions_resources(self.OptionGroup.__name__, option_group)

    def ParameterGroup(self, parameter_group: Union[str, ParameterGroupArn]):
        return self._set_all_actions_resources(self.ParameterGroup.__name__, parameter_group)

    def Proxy(self, proxy: Union[str, ProxyArn]):
        return self._set_all_actions_resources(self.Proxy.__name__, proxy)

    def ReservedInstance(self, reserved_instance: Union[str, ReservedInstanceArn]):
        return self._set_all_actions_resources(self.ReservedInstance.__name__, reserved_instance)

    def SecurityGroup(self, security_group: Union[str, SecurityGroupArn]):
        return self._set_all_actions_resources(self.SecurityGroup.__name__, security_group)

    def Snapshot(self, snapshot: Union[str, SnapshotArn]):
        return self._set_all_actions_resources(self.Snapshot.__name__, snapshot)

    def SubnetGroup(self, subnet_group: Union[str, SubnetGroupArn]):
        return self._set_all_actions_resources(self.SubnetGroup.__name__, subnet_group)

    def Target(self, target: Union[str, TargetArn]):
        return self._set_all_actions_resources(self.Target.__name__, target)

    def TargetGroup(self, target_group: Union[str, TargetGroupArn]):
        return self._set_all_actions_resources(self.TargetGroup.__name__, target_group)

# ----------------------------------------------


class Actions:
    class Write:
        @staticmethod
        def AddRoleToDBCluster(): return RdsAction(Actions.Write.AddRoleToDBCluster.__name__,
                                                   required=[RdsAction.Cluster.__name__])

        @staticmethod
        def AddRoleToDBInstance(): return RdsAction(Actions.Write.AddRoleToDBInstance.__name__,
                                                    required=[RdsAction.DBInstance.__name__])

        @staticmethod
        def AddSourceIdentifierToSubscription(): return RdsAction(Actions.Write.AddSourceIdentifierToSubscription.__name__,
                                                                  required=[RdsAction.EventSubscription.__name__])

        @staticmethod
        def ApplyPendingMaintenanceAction(): return RdsAction(Actions.Write.ApplyPendingMaintenanceAction.__name__,
                                                              required=[RdsAction.DBInstance.__name__])

        @staticmethod
        def BacktrackDBCluster(): return RdsAction(Actions.Write.BacktrackDBCluster.__name__,
                                                   required=[RdsAction.Cluster.__name__])

        @staticmethod
        def CancelExportTask(): return RdsAction(Actions.Write.CancelExportTask.__name__)

        @staticmethod
        def CopyDBClusterParameterGroup(): return RdsAction(Actions.Write.CopyDBClusterParameterGroup.__name__,
                                                            required=[RdsAction.ClusterParameterGroup.__name__])

        @staticmethod
        def CopyDBClusterSnapshot(): return RdsAction(Actions.Write.CopyDBClusterSnapshot.__name__,
                                                      required=[RdsAction.ClusterSnapshot.__name__])

        @staticmethod
        def CopyDBParameterGroup(): return RdsAction(Actions.Write.CopyDBParameterGroup.__name__,
                                                     required=[RdsAction.ParameterGroup.__name__])

        @staticmethod
        def CopyDBSnapshot(): return RdsAction(Actions.Write.CopyDBSnapshot.__name__,
                                               required=[RdsAction.Snapshot.__name__])

        @staticmethod
        def CopyOptionGroup(): return RdsAction(Actions.Write.CopyOptionGroup.__name__,
                                                required=[RdsAction.OptionGroup.__name__])

        @staticmethod
        def CreateDBClusterEndpoint(): return RdsAction(Actions.Write.CreateDBClusterEndpoint.__name__,
                                                        required=[RdsAction.Cluster.__name__,
                                                                  RdsAction.ClusterEndpoint.__name__])

        @staticmethod
        def CreateDBProxy(): return RdsAction(Actions.Write.CreateDBProxy.__name__)

        @staticmethod
        def DeleteDBCluster(): return RdsAction(Actions.Write.DeleteDBCluster.__name__,
                                                required=[RdsAction.Cluster.__name__,
                                                          RdsAction.ClusterSnapshot.__name__])

        @staticmethod
        def DeleteDBClusterEndpoint(): return RdsAction(Actions.Write.DeleteDBClusterEndpoint.__name__,
                                                        required=[RdsAction.ClusterEndpoint.__name__])

        @staticmethod
        def DeleteDBClusterParameterGroup(): return RdsAction(Actions.Write.DeleteDBClusterParameterGroup.__name__,
                                                              required=[RdsAction.ClusterParameterGroup.__name__])

        @staticmethod
        def DeleteDBClusterSnapshot(): return RdsAction(Actions.Write.DeleteDBClusterSnapshot.__name__,
                                                        required=[RdsAction.ClusterSnapshot.__name__])

        @staticmethod
        def DeleteDBInstance(): return RdsAction(Actions.Write.DeleteDBInstance.__name__,
                                                 required=[RdsAction.DBInstance.__name__])

        @staticmethod
        def DeleteDBInstanceAutomatedBackup(): return RdsAction(Actions.Write.DeleteDBInstanceAutomatedBackup.__name__)

        @staticmethod
        def DeleteDBParameterGroup(): return RdsAction(Actions.Write.DeleteDBParameterGroup.__name__,
                                                       required=[RdsAction.ParameterGroup.__name__])

        @staticmethod
        def DeleteDBProxy(): return RdsAction(Actions.Write.DeleteDBProxy.__name__, required=[RdsAction.Proxy.__name__])

        @staticmethod
        def DeleteDBSecurityGroup(): return RdsAction(Actions.Write.DeleteDBSecurityGroup.__name__,
                                                      required=[RdsAction.SecurityGroup.__name__])

        @staticmethod
        def DeleteDBSnapshot(): return RdsAction(Actions.Write.DeleteDBSnapshot.__name__,
                                                 required=[RdsAction.Snapshot.__name__])

        @staticmethod
        def DeleteDBSubnetGroup(): return RdsAction(Actions.Write.DeleteDBSubnetGroup.__name__,
                                                    required=[RdsAction.SubnetGroup.__name__])

        @staticmethod
        def DeleteEventSubscription(): return RdsAction(Actions.Write.DeleteEventSubscription.__name__,
                                                        required=[RdsAction.EventSubscription.__name__])

        @staticmethod
        def DeleteOptionGroup(): return RdsAction(Actions.Write.DeleteOptionGroup.__name__,
                                                  required=[RdsAction.OptionGroup.__name__])

        @staticmethod
        def DeregisterDBProxyTargets(): return RdsAction(Actions.Write.DeregisterDBProxyTargets.__name__,
                                                         required=[RdsAction.Cluster.__name__,
                                                                   RdsAction.DBInstance.__name__,
                                                                   RdsAction.Proxy.__name__,
                                                                   RdsAction.TargetGroup.__name__])

        @staticmethod
        def FailoverDBCluster(): return RdsAction(Actions.Write.FailoverDBCluster.__name__,
                                                  required=[RdsAction.Cluster.__name__])

        @staticmethod
        def ModifyCurrentDBClusterCapacity(): return RdsAction(Actions.Write.ModifyCurrentDBClusterCapacity.__name__,
                                                               required=[RdsAction.Cluster.__name__])

        @staticmethod
        def ModifyDBCluster(): return RdsAction(Actions.Write.ModifyDBCluster.__name__,
                                                required=[RdsAction.Cluster.__name__,
                                                          RdsAction.ClusterParameterGroup.__name__,
                                                          RdsAction.OptionGroup.__name__])

        @staticmethod
        def ModifyDBClusterEndpoint(): return RdsAction(Actions.Write.ModifyDBClusterEndpoint.__name__,
                                                        required=[RdsAction.ClusterEndpoint.__name__])

        @staticmethod
        def ModifyDBClusterParameterGroup(): return RdsAction(Actions.Write.ModifyDBClusterParameterGroup.__name__,
                                                              required=[RdsAction.ClusterParameterGroup.__name__])

        @staticmethod
        def ModifyDBClusterSnapshotAttribute(): return RdsAction(Actions.Write.ModifyDBClusterSnapshotAttribute.__name__,
                                                                 required=[RdsAction.ClusterSnapshot.__name__])

        @staticmethod
        def ModifyDBInstance(): return RdsAction(Actions.Write.ModifyDBInstance.__name__,
                                                 required=[RdsAction.DBInstance.__name__,
                                                           RdsAction.OptionGroup.__name__,
                                                           RdsAction.ParameterGroup.__name__,
                                                           RdsAction.SecurityGroup.__name__])

        @staticmethod
        def ModifyDBParameterGroup(): return RdsAction(Actions.Write.ModifyDBParameterGroup.__name__,
                                                       required=[RdsAction.ParameterGroup.__name__])

        @staticmethod
        def ModifyDBProxy(): return RdsAction(Actions.Write.ModifyDBProxy.__name__, required=[RdsAction.Proxy.__name__])

        @staticmethod
        def ModifyDBProxyTargetGroup(): return RdsAction(Actions.Write.ModifyDBProxyTargetGroup.__name__,
                                                         required=[RdsAction.TargetGroup.__name__])

        @staticmethod
        def ModifyDBSnapshot(): return RdsAction(Actions.Write.ModifyDBSnapshot.__name__,
                                                 required=[RdsAction.Snapshot.__name__])

        @staticmethod
        def ModifyDBSnapshotAttribute(): return RdsAction(Actions.Write.ModifyDBSnapshotAttribute.__name__,
                                                          required=[RdsAction.Snapshot.__name__])

        @staticmethod
        def ModifyDBSubnetGroup(): return RdsAction(Actions.Write.ModifyDBSubnetGroup.__name__,
                                                    required=[RdsAction.SubnetGroup.__name__])

        @staticmethod
        def ModifyEventSubscription(): return RdsAction(Actions.Write.ModifyEventSubscription.__name__,
                                                        required=[RdsAction.EventSubscription.__name__])

        @staticmethod
        def ModifyOptionGroup(): return RdsAction(Actions.Write.ModifyOptionGroup.__name__,
                                                  required=[RdsAction.OptionGroup.__name__])

        @staticmethod
        def PromoteReadReplica(): return RdsAction(Actions.Write.PromoteReadReplica.__name__,
                                                   required=[RdsAction.DBInstance.__name__])

        @staticmethod
        def PromoteReadReplicaDBCluster(): return RdsAction(Actions.Write.PromoteReadReplicaDBCluster.__name__,
                                                            required=[RdsAction.Cluster.__name__])

        @staticmethod
        def PurchaseReservedDBInstancesOffering(): return RdsAction(Actions.Write.PurchaseReservedDBInstancesOffering.__name__,
                                                                    required=[RdsAction.ReservedInstance.__name__])

        @staticmethod
        def RebootDBInstance(): return RdsAction(Actions.Write.RebootDBInstance.__name__,
                                                 required=[RdsAction.DBInstance.__name__])

        @staticmethod
        def RegisterDBProxyTargets(): return RdsAction(Actions.Write.RegisterDBProxyTargets.__name__,
                                                       required=[RdsAction.TargetGroup.__name__])

        @staticmethod
        def RemoveRoleFromDBCluster(): return RdsAction(Actions.Write.RemoveRoleFromDBCluster.__name__,
                                                        required=[RdsAction.Cluster.__name__])

        @staticmethod
        def RemoveRoleFromDBInstance(): return RdsAction(Actions.Write.RemoveRoleFromDBInstance.__name__,
                                                         required=[RdsAction.DBInstance.__name__])

        @staticmethod
        def RemoveSourceIdentifierFromSubscription(): return RdsAction(Actions.Write.RemoveSourceIdentifierFromSubscription.__name__,
                                                                       required=[RdsAction.EventSubscription.__name__])

        @staticmethod
        def ResetDBClusterParameterGroup(): return RdsAction(Actions.Write.ResetDBClusterParameterGroup.__name__,
                                                             required=[RdsAction.ClusterParameterGroup.__name__])

        @staticmethod
        def ResetDBParameterGroup(): return RdsAction(Actions.Write.ResetDBParameterGroup.__name__,
                                                      required=[RdsAction.ParameterGroup.__name__])

        @staticmethod
        def RestoreDBClusterFromS3(): return RdsAction(Actions.Write.RestoreDBClusterFromS3.__name__,
                                                       required=[RdsAction.Cluster.__name__])

        @staticmethod
        def RestoreDBClusterFromSnapshot(): return RdsAction(Actions.Write.RestoreDBClusterFromSnapshot.__name__,
                                                             required=[RdsAction.Cluster.__name__,
                                                                       RdsAction.ClusterSnapshot.__name__,
                                                                       RdsAction.OptionGroup.__name__])

        @staticmethod
        def RestoreDBClusterToPointInTime(): return RdsAction(Actions.Write.RestoreDBClusterToPointInTime.__name__,
                                                              required=[RdsAction.Cluster.__name__,
                                                                        RdsAction.OptionGroup.__name__,
                                                                        RdsAction.SubnetGroup.__name__])

        @staticmethod
        def RestoreDBInstanceFromDBSnapshot(): return RdsAction(Actions.Write.RestoreDBInstanceFromDBSnapshot.__name__,
                                                                required=[RdsAction.DBInstance.__name__,
                                                                          RdsAction.OptionGroup.__name__,
                                                                          RdsAction.Snapshot.__name__,
                                                                          RdsAction.SubnetGroup.__name__])

        @staticmethod
        def RestoreDBInstanceFromS3(): return RdsAction(Actions.Write.RestoreDBInstanceFromS3.__name__,
                                                        required=[RdsAction.DBInstance.__name__])

        @staticmethod
        def RestoreDBInstanceToPointInTime(): return RdsAction(Actions.Write.RestoreDBInstanceToPointInTime.__name__,
                                                               required=[RdsAction.DBInstance.__name__,
                                                                         RdsAction.OptionGroup.__name__,
                                                                         RdsAction.Snapshot.__name__,
                                                                         RdsAction.SubnetGroup.__name__])

        @staticmethod
        def RevokeDBSecurityGroupIngress(): return RdsAction(Actions.Write.RevokeDBSecurityGroupIngress.__name__,
                                                             required=[RdsAction.SecurityGroup.__name__])

        @staticmethod
        def StartActivityStream(): return RdsAction(Actions.Write.StartActivityStream.__name__,
                                                    required=[RdsAction.Cluster.__name__])

        @staticmethod
        def StartDBCluster(): return RdsAction(Actions.Write.StartDBCluster.__name__,
                                               required=[RdsAction.Cluster.__name__])

        @staticmethod
        def StartDBInstance(): return RdsAction(Actions.Write.StartDBInstance.__name__,
                                                required=[RdsAction.DBInstance.__name__])

        @staticmethod
        def StartExportTask(): return RdsAction(Actions.Write.StartExportTask.__name__)

        @staticmethod
        def StopActivityStream(): return RdsAction(Actions.Write.StopActivityStream.__name__,
                                                   required=[RdsAction.Cluster.__name__])

        @staticmethod
        def StopDBCluster(): return RdsAction(Actions.Write.StopDBCluster.__name__,
                                              required=[RdsAction.Cluster.__name__])

        @staticmethod
        def StopDBInstance(): return RdsAction(Actions.Write.StopDBInstance.__name__,
                                               required=[RdsAction.DBInstance.__name__])

    class Read:
        @staticmethod
        def DescribeDBClusterSnapshots(): return RdsAction(Actions.Read.DescribeDBClusterSnapshots.__name__)

        @staticmethod
        def DownloadCompleteDBLogFile(): return RdsAction(Actions.Read.DownloadCompleteDBLogFile.__name__)

        @staticmethod
        def DownloadDBLogFilePortion(): return RdsAction(Actions.Read.DownloadDBLogFilePortion.__name__,
                                                         required=[RdsAction.DBInstance.__name__])

        @staticmethod
        def ListTagsForResource(): return RdsAction(Actions.Read.ListTagsForResource.__name__,
                                                    optional=[RdsAction.DBInstance.__name__,
                                                              RdsAction.EventSubscription.__name__,
                                                              RdsAction.OptionGroup.__name__,
                                                              RdsAction.ParameterGroup.__name__,
                                                              RdsAction.ReservedInstance.__name__,
                                                              RdsAction.SecurityGroup.__name__,
                                                              RdsAction.Snapshot.__name__,
                                                              RdsAction.SubnetGroup.__name__])

    class List:
        @staticmethod
        def DescribeAccountAttributes(): return RdsAction(Actions.List.DescribeAccountAttributes.__name__)

        @staticmethod
        def DescribeCertificates(): return RdsAction(Actions.List.DescribeCertificates.__name__)

        @staticmethod
        def DescribeDBClusterBacktracks(): return RdsAction(Actions.List.DescribeDBClusterBacktracks.__name__,
                                                            required=[RdsAction.Cluster.__name__])

        @staticmethod
        def DescribeDBClusterEndpoints(): return RdsAction(Actions.List.DescribeDBClusterEndpoints.__name__)

        @staticmethod
        def DescribeDBClusterParameterGroups(): return RdsAction(Actions.List.DescribeDBClusterParameterGroups.__name__,
                                                                 required=[RdsAction.ClusterParameterGroup.__name__])

        @staticmethod
        def DescribeDBClusterParameters(): return RdsAction(Actions.List.DescribeDBClusterParameters.__name__,
                                                            required=[RdsAction.ClusterParameterGroup.__name__])

        @staticmethod
        def DescribeDBClusterSnapshotAttributes(): return RdsAction(Actions.List.DescribeDBClusterSnapshotAttributes.__name__,
                                                                    required=[RdsAction.ClusterSnapshot.__name__])

        @staticmethod
        def DescribeDBClusters(): return RdsAction(Actions.List.DescribeDBClusters.__name__,
                                                   required=[RdsAction.Cluster.__name__])

        @staticmethod
        def DescribeDBEngineVersions(): return RdsAction(Actions.List.DescribeDBEngineVersions.__name__,
                                                         required=[RdsAction.ParameterGroup.__name__])

        @staticmethod
        def DescribeDBInstanceAutomatedBackups(): return RdsAction(Actions.List.DescribeDBInstanceAutomatedBackups.__name__)

        @staticmethod
        def DescribeDBInstances(): return RdsAction(Actions.List.DescribeDBInstances.__name__)

        @staticmethod
        def DescribeDBLogFiles(): return RdsAction(Actions.List.DescribeDBLogFiles.__name__,
                                                   required=[RdsAction.DBInstance.__name__])

        @staticmethod
        def DescribeDBParameterGroups(): return RdsAction(Actions.List.DescribeDBParameterGroups.__name__,
                                                          required=[RdsAction.ParameterGroup.__name__])

        @staticmethod
        def DescribeDBParameters(): return RdsAction(Actions.List.DescribeDBParameters.__name__,
                                                     required=[RdsAction.ParameterGroup.__name__])

        @staticmethod
        def DescribeDBProxies(): return RdsAction(Actions.List.DescribeDBProxies.__name__,
                                                  required=[RdsAction.Proxy.__name__])

        @staticmethod
        def DescribeDBProxyTargetGroups(): return RdsAction(Actions.List.DescribeDBProxyTargetGroups.__name__,
                                                            required=[RdsAction.Proxy.__name__])

        @staticmethod
        def DescribeDBProxyTargets(): return RdsAction(Actions.List.DescribeDBProxyTargets.__name__,
                                                       required=[RdsAction.Cluster.__name__,
                                                                 RdsAction.DBInstance.__name__,
                                                                 RdsAction.Proxy.__name__,
                                                                 RdsAction.TargetGroup.__name__])

        @staticmethod
        def DescribeDBSecurityGroups(): return RdsAction(Actions.List.DescribeDBSecurityGroups.__name__,
                                                         required=[RdsAction.SecurityGroup.__name__])

        @staticmethod
        def DescribeDBSnapshotAttributes(): return RdsAction(Actions.List.DescribeDBSnapshotAttributes.__name__,
                                                             required=[RdsAction.Snapshot.__name__])

        @staticmethod
        def DescribeDBSnapshots(): return RdsAction(Actions.List.DescribeDBSnapshots.__name__,
                                                    required=[RdsAction.DBInstance.__name__,
                                                              RdsAction.Snapshot.__name__])

        @staticmethod
        def DescribeDBSubnetGroups(): return RdsAction(Actions.List.DescribeDBSubnetGroups.__name__,
                                                       required=[RdsAction.SubnetGroup.__name__])

        @staticmethod
        def DescribeEngineDefaultClusterParameters(): return RdsAction(Actions.List.DescribeEngineDefaultClusterParameters.__name__)

        @staticmethod
        def DescribeEngineDefaultParameters(): return RdsAction(Actions.List.DescribeEngineDefaultParameters.__name__)

        @staticmethod
        def DescribeEventCategories(): return RdsAction(Actions.List.DescribeEventCategories.__name__)

        @staticmethod
        def DescribeEventSubscriptions(): return RdsAction(Actions.List.DescribeEventSubscriptions.__name__,
                                                           required=[RdsAction.EventSubscription.__name__])

        @staticmethod
        def DescribeEvents(): return RdsAction(Actions.List.DescribeEvents.__name__,
                                               required=[RdsAction.EventSubscription.__name__])

        @staticmethod
        def DescribeExportTasks(): return RdsAction(Actions.List.DescribeExportTasks.__name__)

        @staticmethod
        def DescribeOptionGroupOptions(): return RdsAction(Actions.List.DescribeOptionGroupOptions.__name__,
                                                           required=[RdsAction.OptionGroup.__name__])

        @staticmethod
        def DescribeOptionGroups(): return RdsAction(Actions.List.DescribeOptionGroups.__name__,
                                                     required=[RdsAction.OptionGroup.__name__])

        @staticmethod
        def DescribeOrderableDBInstanceOptions(): return RdsAction(Actions.List.DescribeOrderableDBInstanceOptions.__name__)

        @staticmethod
        def DescribePendingMaintenanceActions(): return RdsAction(Actions.List.DescribePendingMaintenanceActions.__name__,
                                                                  required=[RdsAction.DBInstance.__name__])

        @staticmethod
        def DescribeReservedDBInstances(): return RdsAction(Actions.List.DescribeReservedDBInstances.__name__,
                                                            required=[RdsAction.ReservedInstance.__name__])

        @staticmethod
        def DescribeReservedDBInstancesOfferings(): return RdsAction(Actions.List.DescribeReservedDBInstancesOfferings.__name__)

        @staticmethod
        def DescribeSourceRegions(): return RdsAction(Actions.List.DescribeSourceRegions.__name__)

        @staticmethod
        def DescribeValidDBInstanceModifications(): return RdsAction(Actions.List.DescribeValidDBInstanceModifications.__name__,
                                                                     required=[RdsAction.DBInstance.__name__])

    class Tagging:
        @staticmethod
        def AddTagsToResource(): return RdsAction(Actions.Tagging.AddTagsToResource.__name__,
                                                  optional=[RdsAction.DBInstance.__name__,
                                                            RdsAction.EventSubscription.__name__,
                                                            RdsAction.OptionGroup.__name__,
                                                            RdsAction.ParameterGroup.__name__,
                                                            RdsAction.ReservedInstance.__name__,
                                                            RdsAction.SecurityGroup.__name__,
                                                            RdsAction.Snapshot.__name__,
                                                            RdsAction.SubnetGroup.__name__])

        @staticmethod
        def CreateDBCluster(): return RdsAction(Actions.Tagging.CreateDBCluster.__name__,
                                                required=[RdsAction.Cluster.__name__,
                                                          RdsAction.ClusterParameterGroup.__name__,
                                                          RdsAction.OptionGroup.__name__,
                                                          RdsAction.SubnetGroup.__name__])

        @staticmethod
        def CreateDBClusterParameterGroup(): return RdsAction(Actions.Tagging.CreateDBClusterParameterGroup.__name__,
                                                              required=[RdsAction.ClusterParameterGroup.__name__])

        @staticmethod
        def CreateDBClusterSnapshot(): return RdsAction(Actions.Tagging.CreateDBClusterSnapshot.__name__,
                                                        required=[RdsAction.Cluster.__name__,
                                                                  RdsAction.ClusterSnapshot.__name__])

        @staticmethod
        def CreateDBInstance(): return RdsAction(Actions.Tagging.CreateDBInstance.__name__,
                                                 required=[RdsAction.DBInstance.__name__,
                                                           RdsAction.OptionGroup.__name__,
                                                           RdsAction.ParameterGroup.__name__,
                                                           RdsAction.SecurityGroup.__name__,
                                                           RdsAction.SubnetGroup.__name__])

        @staticmethod
        def CreateDBInstanceReadReplica(): return RdsAction(Actions.Tagging.CreateDBInstanceReadReplica.__name__,
                                                            required=[RdsAction.DBInstance.__name__,
                                                                      RdsAction.OptionGroup.__name__,
                                                                      RdsAction.SubnetGroup.__name__])

        @staticmethod
        def CreateDBParameterGroup(): return RdsAction(Actions.Tagging.CreateDBParameterGroup.__name__,
                                                       required=[RdsAction.ParameterGroup.__name__])

        @staticmethod
        def CreateDBSecurityGroup(): return RdsAction(Actions.Tagging.CreateDBSecurityGroup.__name__,
                                                      required=[RdsAction.SecurityGroup.__name__])

        @staticmethod
        def CreateDBSnapshot(): return RdsAction(Actions.Tagging.CreateDBSnapshot.__name__,
                                                 required=[RdsAction.DBInstance.__name__,
                                                           RdsAction.Snapshot.__name__])

        @staticmethod
        def CreateDBSubnetGroup(): return RdsAction(Actions.Tagging.CreateDBSubnetGroup.__name__,
                                                    required=[RdsAction.SubnetGroup.__name__])

        @staticmethod
        def CreateEventSubscription(): return RdsAction(Actions.Tagging.CreateEventSubscription.__name__,
                                                        required=[RdsAction.EventSubscription.__name__])

        @staticmethod
        def CreateOptionGroup(): return RdsAction(Actions.Tagging.CreateOptionGroup.__name__,
                                                  required=[RdsAction.OptionGroup.__name__])

        @staticmethod
        def RemoveTagsFromResource(): return RdsAction(Actions.Tagging.RemoveTagsFromResource.__name__,
                                                       optional=[RdsAction.DBInstance.__name__,
                                                                 RdsAction.EventSubscription.__name__,
                                                                 RdsAction.OptionGroup.__name__,
                                                                 RdsAction.ParameterGroup.__name__,
                                                                 RdsAction.ReservedInstance.__name__,
                                                                 RdsAction.SecurityGroup.__name__,
                                                                 RdsAction.Snapshot.__name__,
                                                                 RdsAction.SubnetGroup.__name__])

    class PermissionManagement:
        @staticmethod
        def AuthorizeDBSecurityGroupIngress(): return RdsAction(Actions.PermissionManagement.AuthorizeDBSecurityGroupIngress.__name__,
                                                                required=[RdsAction.SecurityGroup.__name__])

    @staticmethod
    def WriteAll(): return RdsAccessLevellAllActions(Actions.Write)

    @staticmethod
    def ReadAll(): return RdsAccessLevellAllActions(Actions.Write)

    @staticmethod
    def ListAll(): return RdsAccessLevellAllActions(Actions.List)

    @staticmethod
    def TaggingAll(): return RdsAccessLevellAllActions(Actions.Write)

    @staticmethod
    def PermissionManagementAll(): return RdsAccessLevellAllActions(Actions.PermissionManagement)

    All = "rds:*"
