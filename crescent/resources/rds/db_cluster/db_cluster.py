from crescent.core import Resource, Tag, AllowedValues as CoreAllowedValues
from crescent.functions import AnyFn
from .db_cluster_role import DBClusterRole
from .scaling_configuration import ScalingConfiguration
from .constants import AllowedValues, Conditions, NotSpecifyIfSpecified, ResourceRequiredProperties
from typing import Union


class DBCluster(Resource):
    __TYPE = "AWS::RDS::DBCluster"

    def __init__(self, id: str):
        super(DBCluster, self).__init__(
            id=id,
            type=self.__TYPE,
            allowed_values={self.AvailabilityZones.__name__: CoreAllowedValues.ZONE,
                            self.Engine.__name__: AllowedValues.ENGINE,
                            self.EngineMode.__name__: AllowedValues.ENGINE_MODE,
                            self.RestoreType.__name__: AllowedValues.RESTORE_TYPE},
            min_value={self.BacktrackWindow.__name__: 0,
                       self.BackupRetentionPeriod.__name__: 1},
            max_value={self.BacktrackWindow.__name__: 259200,
                       self.BackupRetentionPeriod.__name__: 35},
            not_specify_if_specified={self.MasterUsername.__name__: NotSpecifyIfSpecified.DB_CLUSTER_MASTER_USERNAME,
                                      self.MasterUserPassword.__name__: NotSpecifyIfSpecified.DB_CLUSTER_MASTER_USER_PASSWORD,
                                      self.StorageEncrypted.__name__: NotSpecifyIfSpecified.DB_CLUSTER_STORAGE_ENCRYPTED},
            conditions={self.EngineVersion.__name__: Conditions.ENGINE_VERSION,
                        self.ScalingConfiguration.__name__: Conditions.SCALING_CONFIGURATION},
            required_properties=ResourceRequiredProperties.DB_CLUSTER
        )

    def AssociatedRoles(self, *associated_roles: DBClusterRole):
        return self._set_property(self.AssociatedRoles.__name__, list(associated_roles))

    def AvailabilityZones(self, *availability_zones: Union[str, AnyFn]):
        return self._set_property(self.AvailabilityZones.__name__, list(availability_zones))

    def BacktrackWindow(self, backtrack_window: Union[int, AnyFn]):
        return self._set_property(self.BacktrackWindow.__name__, backtrack_window)

    def BackupRetentionPeriod(self, backup_retention_period: Union[int, AnyFn]):
        return self._set_property(self.BackupRetentionPeriod.__name__, backup_retention_period)

    def DatabaseName(self, database_name: Union[str, AnyFn]):
        return self._set_property(self.DatabaseName.__name__, database_name)

    def DBClusterIdentifier(self, db_cluster_identifier: Union[str, AnyFn]):
        return self._set_property(self.DBClusterIdentifier.__name__, db_cluster_identifier)

    def DBClusterParameterGroupName(self, db_cluster_pg_name: Union[str, AnyFn]):
        return self._set_property(self.DBClusterParameterGroupName.__name__, db_cluster_pg_name)

    def DBSubnetGroupName(self, db_subnet_group_name: Union[str, AnyFn]):
        return self._set_property(self.DBSubnetGroupName.__name__, db_subnet_group_name)

    def DeletionProtection(self, deletion_protection: Union[bool, AnyFn]):
        return self._set_property(self.DeletionProtection.__name__, deletion_protection)

    def EnableCloudwatchLogsExports(self, *enable_cw_logs_exports: Union[str, AnyFn]):
        return self._set_property(self.EnableCloudwatchLogsExports.__name__, list(enable_cw_logs_exports))

    def EnableHttpEndpoint(self, enable_http_endpoint: Union[bool, AnyFn]):
        return self._set_property(self.EnableHttpEndpoint.__name__, enable_http_endpoint)

    def EnableIAMDatabaseAuthentication(self, enable_iam_db_auth: Union[bool, AnyFn]):
        return self._set_property(self.EnableIAMDatabaseAuthentication.__name__, enable_iam_db_auth)

    def Engine(self, engine: Union[str, AnyFn]):
        return self._set_property(self.Engine.__name__, engine)

    def EngineMode(self, engine_mode: Union[str, AnyFn]):
        return self._set_property(self.EngineMode.__name__, engine_mode)

    def EngineVersion(self, engine_version: Union[str, AnyFn]):
        return self._set_property(self.EngineVersion.__name__, engine_version)

    def KmsKeyId(self, kms_key_id: Union[str, AnyFn]):
        return self._set_property(self.KmsKeyId.__name__, kms_key_id)

    def MasterUsername(self, master_username: Union[str, AnyFn]):
        return self._set_property(self.MasterUsername.__name__, master_username)

    def MasterUserPassword(self, master_user_password: Union[str, AnyFn]):
        return self._set_property(self.MasterUserPassword.__name__, master_user_password)

    def Port(self, port: Union[int, AnyFn]):
        return self._set_property(self.Port.__name__, port)

    def PreferredBackupWindow(self, preffered_backup_window: Union[str, AnyFn]):
        return self._set_property(self.PreferredBackupWindow.__name__, preffered_backup_window)

    def PreferredMaintenanceWindow(self, preferred_maintenance_window: Union[str, AnyFn]):
        return self._set_property(self.PreferredMaintenanceWindow.__name__, preferred_maintenance_window)

    def ReplicationSourceIdentifier(self, replication_source_identifier: Union[str, AnyFn]):
        return self._set_property(self.ReplicationSourceIdentifier.__name__, replication_source_identifier)

    def RestoreType(self, restore_type: Union[str, AnyFn]):
        return self._set_property(self.RestoreType.__name__, restore_type)

    def ScalingConfiguration(self, scaling_conf: ScalingConfiguration):
        return self._set_property(self.ScalingConfiguration.__name__, scaling_conf)

    def SnapshotIdentifier(self, snapshot_identifier: Union[str, AnyFn]):
        return self._set_property(self.SnapshotIdentifier.__name__, snapshot_identifier)

    def SourceDBClusterIdentifier(self, source_db_cluster_identifier: Union[str, AnyFn]):
        return self._set_property(self.SourceDBClusterIdentifier.__name__, source_db_cluster_identifier)

    def SourceRegion(self, source_region: Union[str, AnyFn]):
        return self._set_property(self.SourceRegion.__name__, source_region)

    def StorageEncrypted(self, storage_encrypted: Union[bool, AnyFn]):
        return self._set_property(self.StorageEncrypted.__name__, storage_encrypted)

    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))

    def UseLatestRestorableTime(self, use_latest_restorable_time: Union[bool, AnyFn]):
        return self._set_property(self.UseLatestRestorableTime.__name__, use_latest_restorable_time)

    def VpcSecurityGroupIds(self, *vpc_security_group_ids: Union[str, AnyFn]):
        return self._set_property(self.VpcSecurityGroupIds.__name__, list(vpc_security_group_ids))
