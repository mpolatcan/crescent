from pyformation import PyformationResource, Tag
from .db_cluster_role import DBClusterRole
from .scaling_configuration import ScalingConfiguration


class DBCluster(PyformationResource):
    __TYPE = "AWS::RDS::DBCluster"

    def __init__(self, id: str):
        super(DBCluster, self).__init__(id, self.__TYPE)

    def AssociatedRoles(self, *value: DBClusterRole):
        return self._set_property(self.AssociatedRoles.__name__, [dcr.__to_dict__() for dcr in list(value)])

    def AvailabilityZones(self, *value: str):
        return self._set_property(self.AvailabilityZones.__name__, list(value))

    def BacktrackWindow(self, value: int):
        return self._set_property(self.BacktrackWindow.__name__, value)

    def BackupRetentionPeriod(self, value: int):
        return self._set_property(self.BackupRetentionPeriod.__name__, value)

    def DatabaseName(self, value: str):
        return self._set_property(self.DatabaseName.__name__, value)

    def DBClusterIdentifier(self, value: str):
        return self._set_property(self.DBClusterIdentifier.__name__, value)

    def DBClusterParameterGroupName(self, value: str):
        return self._set_property(self.DBClusterParameterGroupName.__name__, value)

    def DBSubnetGroupName(self, value: str):
        return self._set_property(self.DBSubnetGroupName.__name__, value)

    def DeletionProtection(self, value: bool):
        return self._set_property(self.DeletionProtection.__name__, value)

    def EnableCloudwatchLogsExports(self, *value: str):
        return self._set_property(self.EnableCloudwatchLogsExports.__name__, list(value))

    def EnableHttpEndpoint(self, value: bool):
        return self._set_property(self.EnableHttpEndpoint.__name__, value)

    def EnableIAMDatabaseAuthentication(self, value: bool):
        return self._set_property(self.EnableIAMDatabaseAuthentication.__name__, value)

    def Engine(self, value: str):
        return self._set_property(self.Engine.__name__, value)

    def EngineMode(self, value: str):
        return self._set_property(self.EngineMode.__name__, value)

    def EngineVersion(self, value: str):
        return self._set_property(self.EngineVersion.__name__, value)

    def KmsKeyId(self, value: str):
        return self._set_property(self.KmsKeyId.__name__, value)

    def MasterUsername(self, value: str):
        return self._set_property(self.MasterUsername.__name__, value)

    def MasterUserPassword(self, value: str):
        return self._set_property(self.MasterUserPassword.__name__, value)

    def Port(self, value: int):
        return self._set_property(self.Port.__name__, value)

    def PreferredBackupWindow(self, value: str):
        return self._set_property(self.PreferredBackupWindow.__name__, value)

    def PreferredMaintenanceWindow(self, value: str):
        return self._set_property(self.PreferredMaintenanceWindow.__name__, value)

    def ReplicationSourceIdentifier(self, value: str):
        return self._set_property(self.ReplicationSourceIdentifier.__name__, value)

    def RestoreType(self, value: str):
        return self._set_property(self.RestoreType.__name__, value)

    def ScalingConfiguration(self, value: ScalingConfiguration):
        return self._set_property(self.ScalingConfiguration.__name__, value.__to_dict__())

    def SnapshotIdentifier(self, value: str):
        return self._set_property(self.SnapshotIdentifier.__name__, value)

    def SourceDBClusterIdentifier(self, value: str):
        return self._set_property(self.SourceDBClusterIdentifier.__name__, value)

    def SourceRegion(self, value: str):
        return self._set_property(self.SourceRegion.__name__, value)

    def StorageEncrypted(self, value: bool):
        return self._set_property(self.StorageEncrypted.__name__, value)

    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))

    def UseLatestRestorableTime(self, value: bool):
        return self._set_property(self.UseLatestRestorableTime.__name__, value)

    def VpcSecurityGroupIds(self, *value: str):
        return self._set_property(self.VpcSecurityGroupIds.__name__, list(value))
