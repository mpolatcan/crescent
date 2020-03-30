from crescent.core import Resource, Tag, Validator, AllowedValues as CoreAllowedValues
from .db_cluster_role import DBClusterRole
from .scaling_configuration import ScalingConfiguration
from .constants import AllowedValues, ModelRequiredProperties, Conditions, NotSpecifyIfSpecified


class DBCluster(Resource):
    __TYPE = "AWS::RDS::DBCluster"

    def __init__(self, id: str):
        super(DBCluster, self).__init__(id, self.__TYPE)

    @Validator.validate(type=DBClusterRole, required_properties=ModelRequiredProperties.DB_CLUSTER_ROLE)
    def AssociatedRoles(self, *associated_roles: DBClusterRole):
        return self._set_property(self.AssociatedRoles.__name__, [dcr.__to_dict__() for dcr in list(associated_roles)])

    @Validator.validate(type=str, allowed_values=CoreAllowedValues.ZONE)
    def AvailabilityZones(self, *availability_zones: str):
        return self._set_property(self.AvailabilityZones.__name__, list(availability_zones))

    @Validator.validate(type=int, min_value=0, max_value=259200)
    def BacktrackWindow(self, backtrack_window: int):
        return self._set_property(self.BacktrackWindow.__name__, backtrack_window)

    @Validator.validate(type=int, min_value=1, max_value=35)
    def BackupRetentionPeriod(self, backup_retention_period: int):
        return self._set_property(self.BackupRetentionPeriod.__name__, backup_retention_period)

    @Validator.validate(type=str)
    def DatabaseName(self, database_name: str):
        return self._set_property(self.DatabaseName.__name__, database_name)

    @Validator.validate(type=str)
    def DBClusterIdentifier(self, db_cluster_identifier: str):
        return self._set_property(self.DBClusterIdentifier.__name__, db_cluster_identifier)

    @Validator.validate(type=str)
    def DBClusterParameterGroupName(self, db_cluster_pg_name: str):
        return self._set_property(self.DBClusterParameterGroupName.__name__, db_cluster_pg_name)

    @Validator.validate(type=str)
    def DBSubnetGroupName(self, db_subnet_group_name: str):
        return self._set_property(self.DBSubnetGroupName.__name__, db_subnet_group_name)

    @Validator.validate(type=bool)
    def DeletionProtection(self, deletion_protection: bool):
        return self._set_property(self.DeletionProtection.__name__, deletion_protection)

    @Validator.validate(type=str)
    def EnableCloudwatchLogsExports(self, *enable_cw_logs_exports: str):
        return self._set_property(self.EnableCloudwatchLogsExports.__name__, list(enable_cw_logs_exports))

    @Validator.validate(type=bool)
    def EnableHttpEndpoint(self, enable_http_endpoint: bool):
        return self._set_property(self.EnableHttpEndpoint.__name__, enable_http_endpoint)

    @Validator.validate(type=bool)
    def EnableIAMDatabaseAuthentication(self, enable_iam_db_auth: bool):
        return self._set_property(self.EnableIAMDatabaseAuthentication.__name__, enable_iam_db_auth)

    @Validator.validate(type=str, allowed_values=AllowedValues.ENGINE)
    def Engine(self, engine: str):
        return self._set_property(self.Engine.__name__, engine)

    @Validator.validate(type=str, allowed_values=AllowedValues.ENGINE_MODE)
    def EngineMode(self, engine_mode: str):
        return self._set_property(self.EngineMode.__name__, engine_mode)

    @Validator.validate(type=str, conditions=Conditions.ENGINE_VERSION)
    def EngineVersion(self, engine_version: str):
        return self._set_property(self.EngineVersion.__name__, engine_version)

    @Validator.validate(type=str)
    def KmsKeyId(self, kms_key_id: str):
        return self._set_property(self.KmsKeyId.__name__, kms_key_id)

    @Validator.validate(type=str, not_specify_if_specified=NotSpecifyIfSpecified.DB_CLUSTER_MASTER_USERNAME)
    def MasterUsername(self, master_username: str):
        return self._set_property(self.MasterUsername.__name__, master_username)

    @Validator.validate(type=str, not_specify_if_specified=NotSpecifyIfSpecified.DB_CLUSTER_MASTER_USER_PASSWORD)
    def MasterUserPassword(self, master_user_password: str):
        return self._set_property(self.MasterUserPassword.__name__, master_user_password)

    @Validator.validate(type=int)
    def Port(self, port: int):
        return self._set_property(self.Port.__name__, port)

    @Validator.validate(type=str)
    def PreferredBackupWindow(self, preffered_backup_window: str):
        return self._set_property(self.PreferredBackupWindow.__name__, preffered_backup_window)

    @Validator.validate(type=str)
    def PreferredMaintenanceWindow(self, preferred_maintenance_window: str):
        return self._set_property(self.PreferredMaintenanceWindow.__name__, preferred_maintenance_window)

    @Validator.validate(type=str)
    def ReplicationSourceIdentifier(self, replication_source_identifier: str):
        return self._set_property(self.ReplicationSourceIdentifier.__name__, replication_source_identifier)

    @Validator.validate(type=str, allowed_values=AllowedValues.RESTORE_TYPE)
    def RestoreType(self, restore_type: str):
        return self._set_property(self.RestoreType.__name__, restore_type)

    @Validator.validate(type=ScalingConfiguration, conditions=Conditions.SCALING_CONFIGURATION)
    def ScalingConfiguration(self, scaling_conf: ScalingConfiguration):
        return self._set_property(self.ScalingConfiguration.__name__, scaling_conf.__to_dict__())

    @Validator.validate(type=str)
    def SnapshotIdentifier(self, snapshot_identifier: str):
        return self._set_property(self.SnapshotIdentifier.__name__, snapshot_identifier)

    @Validator.validate(type=str)
    def SourceDBClusterIdentifier(self, source_db_cluster_identifier: str):
        return self._set_property(self.SourceDBClusterIdentifier.__name__, source_db_cluster_identifier)

    @Validator.validate(type=str)
    def SourceRegion(self, source_region: str):
        return self._set_property(self.SourceRegion.__name__, source_region)

    @Validator.validate(type=bool, not_specify_if_specified=NotSpecifyIfSpecified.DB_CLUSTER_STORAGE_ENCRYPTED)
    def StorageEncrypted(self, storage_encrypted: bool):
        return self._set_property(self.StorageEncrypted.__name__, storage_encrypted)

    @Validator.validate(type=Tag)
    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))

    @Validator.validate(type=bool)
    def UseLatestRestorableTime(self, use_latest_restorable_time: bool):
        return self._set_property(self.UseLatestRestorableTime.__name__, use_latest_restorable_time)

    @Validator.validate(type=str)
    def VpcSecurityGroupIds(self, *vpc_security_group_ids: str):
        return self._set_property(self.VpcSecurityGroupIds.__name__, list(vpc_security_group_ids))
