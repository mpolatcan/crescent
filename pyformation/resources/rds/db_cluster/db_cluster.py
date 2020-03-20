from pyformation.core import Resource, Tag, Validator
from .db_cluster_role import DBClusterRole
from .scaling_configuration import ScalingConfiguration
from .constants import Engine, EngineMode, RestoreType, Property, Conditions


class DBCluster(Resource):
    __TYPE = "AWS::RDS::DBCluster"

    def __init__(self, id: str):
        super(DBCluster, self).__init__(id, self.__TYPE)

    @Validator.validate(type=DBClusterRole)
    def AssociatedRoles(self, *value: DBClusterRole):
        return self._set_property(self.AssociatedRoles.__name__, [dcr.__to_dict__() for dcr in list(value)])

    @Validator.validate(type=str)
    def AvailabilityZones(self, *value: str):
        return self._set_property(self.AvailabilityZones.__name__, list(value))

    @Validator.validate(type=int, min_value=0, max_value=259200)
    def BacktrackWindow(self, value: int):
        return self._set_property(self.BacktrackWindow.__name__, value)

    @Validator.validate(type=int, min_value=1, max_value=35)
    def BackupRetentionPeriod(self, value: int):
        return self._set_property(self.BackupRetentionPeriod.__name__, value)

    @Validator.validate(type=str)
    def DatabaseName(self, value: str):
        return self._set_property(self.DatabaseName.__name__, value)

    @Validator.validate(type=str)
    def DBClusterIdentifier(self, value: str):
        return self._set_property(self.DBClusterIdentifier.__name__, value)

    @Validator.validate(type=str)
    def DBClusterParameterGroupName(self, value: str):
        return self._set_property(self.DBClusterParameterGroupName.__name__, value)

    @Validator.validate(type=str)
    def DBSubnetGroupName(self, value: str):
        return self._set_property(self.DBSubnetGroupName.__name__, value)

    @Validator.validate(type=bool)
    def DeletionProtection(self, value: bool):
        return self._set_property(self.DeletionProtection.__name__, value)

    @Validator.validate(type=str)
    def EnableCloudwatchLogsExports(self, *value: str):
        return self._set_property(self.EnableCloudwatchLogsExports.__name__, list(value))

    @Validator.validate(type=bool)
    def EnableHttpEndpoint(self, value: bool):
        return self._set_property(self.EnableHttpEndpoint.__name__, value)

    @Validator.validate(type=bool)
    def EnableIAMDatabaseAuthentication(self, value: bool):
        return self._set_property(self.EnableIAMDatabaseAuthentication.__name__, value)

    @Validator.validate(type=str, allowed_values=[Engine.AURORA,
                                                  Engine.AURORA_MYSQL,
                                                  Engine.AURORA_POSTGRESQL])
    def Engine(self, value: str):
        return self._set_property(self.Engine.__name__, value)

    @Validator.validate(type=str, allowed_values=[EngineMode.PROVISIONED,
                                                  EngineMode.SERVERLESS,
                                                  EngineMode.PARALLEL_QUERY,
                                                  EngineMode.GLOBAL,
                                                  EngineMode.MULTI_MASTER])
    def EngineMode(self, value: str):
        return self._set_property(self.EngineMode.__name__, value)

    @Validator.validate(type=str)
    def EngineVersion(self, value: str):
        return self._set_property(self.EngineVersion.__name__, value)

    @Validator.validate(type=str)
    def KmsKeyId(self, value: str):
        return self._set_property(self.KmsKeyId.__name__, value)

    @Validator.validate(type=str, not_specify_if_specified=[Property.SNAPSHOT_IDENTIFIER])
    def MasterUsername(self, value: str):
        return self._set_property(self.MasterUsername.__name__, value)

    @Validator.validate(type=str, not_specify_if_specified=[Property.SOURCE_DB_INSTANCE_IDENTIFIER,
                                                            Property.SNAPSHOT_IDENTIFIER])
    def MasterUserPassword(self, value: str):
        return self._set_property(self.MasterUserPassword.__name__, value)

    @Validator.validate(type=int)
    def Port(self, value: int):
        return self._set_property(self.Port.__name__, value)

    @Validator.validate(type=str)
    def PreferredBackupWindow(self, value: str):
        return self._set_property(self.PreferredBackupWindow.__name__, value)

    @Validator.validate(type=str)
    def PreferredMaintenanceWindow(self, value: str):
        return self._set_property(self.PreferredMaintenanceWindow.__name__, value)

    @Validator.validate(type=str)
    def ReplicationSourceIdentifier(self, value: str):
        return self._set_property(self.ReplicationSourceIdentifier.__name__, value)

    @Validator.validate(type=str, allowed_values=[RestoreType.FULL_COPY, RestoreType.COPY_ON_WRITE])
    def RestoreType(self, value: str):
        return self._set_property(self.RestoreType.__name__, value)

    @Validator.validate(type=ScalingConfiguration, conditions=Conditions.SCALING_CONFIGURATION)
    def ScalingConfiguration(self, value: ScalingConfiguration):
        return self._set_property(self.ScalingConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=str)
    def SnapshotIdentifier(self, value: str):
        return self._set_property(self.SnapshotIdentifier.__name__, value)

    @Validator.validate(type=str)
    def SourceDBClusterIdentifier(self, value: str):
        return self._set_property(self.SourceDBClusterIdentifier.__name__, value)

    @Validator.validate(type=str)
    def SourceRegion(self, value: str):
        return self._set_property(self.SourceRegion.__name__, value)

    @Validator.validate(type=bool, not_specify_if_specified=[Property.DB_CLUSTER_IDENTIFIER,
                                                             Property.SNAPSHOT_IDENTIFIER,
                                                             Property.SOURCE_DB_INSTANCE_IDENTIFIER])
    def StorageEncrypted(self, value: bool):
        return self._set_property(self.StorageEncrypted.__name__, value)

    @Validator.validate(type=Tag)
    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))

    @Validator.validate(type=bool)
    def UseLatestRestorableTime(self, value: bool):
        return self._set_property(self.UseLatestRestorableTime.__name__, value)

    @Validator.validate(type=str)
    def VpcSecurityGroupIds(self, *value: str):
        return self._set_property(self.VpcSecurityGroupIds.__name__, list(value))
