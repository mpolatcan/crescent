from typing import List
from resources.shared import BaseCloudFormationResourceModel, Tag
from resources.rds.db_cluster import DBClusterRole
from resources.rds.db_cluster import ScalingConfiguration


class DBCluster(BaseCloudFormationResourceModel):
    __TYPE = "AWS::RDS::DBCluster"
    __PROPERTY_ASSOCIATED_ROLES = "AssociatedRoles"
    __PROPERTY_AVAILABILITY_ZONES = "AvailabilityZones"
    __PROPERTY_BACKTRACK_WINDOW = "BacktrackWindow"
    __PROPERTY_BACKUP_RETENTION_PERIOD = "BackupRetentionPeriod"
    __PROPERTY_DATABASE_NAME = "DatabaseName"
    __PROPERTY_DB_CLUSTER_IDENTIFIER = "DBClusterIdentifier"
    __PROPERTY_DB_CLUSTER_PARAMETER_GROUP_NAME = "DBClusterParameterGroupName"
    __PROPERTY_DB_SUBNET_GROUP_NAME = "DBSubnetGroupName"
    __PROPERTY_DELETION_PROTECTION = "DeletionProtection"
    __PROPERTY_ENABLE_CLOUDWATCH_LOGS_EXPORTS = "EnableCloudwatchLogsExports"
    __PROPERTY_ENABLE_HTTP_ENDPOINT = "EnableHttpEndpoint"
    __PROPERTY_ENABLE_IAM_DATABASE_AUTHENTICATION = "EnableIAMDatabaseAuthentication"
    __PROPERTY_ENGINE = "Engine"
    __PROPERTY_ENGINE_MODE = "EngineMode"
    __PROPERTY_ENGINE_VERSION = "EngineVersion"
    __PROPERTY_KMS_KEY_ID = "KmsKeyId"
    __PROPERTY_MASTER_USERNAME = "MasterUsername"
    __PROPERTY_MASTER_USER_PASSWORD = "MasterUserPassword"
    __PROPERTY_PORT = "Port"
    __PROPERTY_PREFERRED_BACKUP_WINDOW = "PreferredBackupWindow"
    __PROPERTY_PREFERRED_MAINTENANCE_WINDOW = "PreferredMaintenanceWindow"
    __PROPERTY_REPLICATION_SOURCE_IDENTIFIER = "ReplicationSourceIdentifier"
    __PROPERTY_RESTORE_TYPE = "RestoreType"
    __PROPERTY_SCALING_CONFIGURATION = "ScalingConfiguration"
    __PROPERTY_SNAPSHOT_IDENTIFIER = "SnapshotIdentifier"
    __PROPERTY_SOURCE_DB_CLUSTER_IDENTIFIER = "SourceDBClusterIdentifier"
    __PROPERTY_SOURCE_REGION = "SourceRegion"
    __PROPERTY_STORAGE_ENCRYPTED = "StorageEncrypted"
    __PROPERTY_TAGS = "Tags"
    __PROPERTY_USE_LATEST_RESTORABLE_TIME = "UseLatestRestorableTime"
    __PROPERTY_VPC_SECURITY_GROUP_IDS = "VpcSecurityGroupIds"

    def __init__(self):
        super(DBCluster, self).__init__(type=self.__TYPE)

    def associated_roles(self, value: List[DBClusterRole]):
        return self._add_property_field(self.__PROPERTY_ASSOCIATED_ROLES, [
            dbc_role.create() for dbc_role in value.create()
        ])

    def availability_zones(self, value: List[str]):
        return self._add_property_field(self.__PROPERTY_AVAILABILITY_ZONES, value)

    def backtrack_window(self, value: int):
        return self._add_property_field(self.__PROPERTY_BACKTRACK_WINDOW, value)

    def backup_retention_period(self, value: int):
        return self._add_property_field(self.__PROPERTY_BACKUP_RETENTION_PERIOD, value)

    def database_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_DATABASE_NAME, value)

    def db_cluster_identifier(self, value: str):
        return self._add_property_field(self.__PROPERTY_DB_CLUSTER_IDENTIFIER, value)

    def db_cluster_parameter_group_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_DB_CLUSTER_PARAMETER_GROUP_NAME, value)

    def db_subnet_group_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_DB_SUBNET_GROUP_NAME, value)

    def deletion_protection(self, value: bool):
        return self._add_property_field(self.__PROPERTY_DELETION_PROTECTION, value)

    def enable_cloudwatch_logs_exports(self, value: List[str]):
        return self._add_property_field(self.__PROPERTY_ENABLE_CLOUDWATCH_LOGS_EXPORTS, value)

    def enable_http_endpoint(self, value: bool):
        return self._add_property_field(self.__PROPERTY_ENABLE_HTTP_ENDPOINT, value)

    def enable_iam_database_authentication(self, value: bool):
        return self._add_property_field(self.__PROPERTY_ENABLE_IAM_DATABASE_AUTHENTICATION, value)

    def engine(self, value: str):
        return self._add_property_field(self.__PROPERTY_ENGINE, value)

    def engine_mode(self, value: str):
        return self._add_property_field(self.__PROPERTY_ENGINE_MODE, value)

    def engine_version(self, value: str):
        return self._add_property_field(self.__PROPERTY_ENGINE_VERSION, value)

    def kms_key_id(self, value: str):
        return self._add_property_field(self.__PROPERTY_KMS_KEY_ID, value)

    def master_username(self, value: str):
        return self._add_property_field(self.__PROPERTY_MASTER_USERNAME, value)

    def master_user_password(self, value: str):
        return self._add_property_field(self.__PROPERTY_MASTER_USER_PASSWORD, value)

    def port(self, value: int):
        return self._add_property_field(self.__PROPERTY_PORT, value)

    def preffered_backup_window(self, value: str):
        return self._add_property_field(self.__PROPERTY_PREFERRED_BACKUP_WINDOW, value)

    def preferred_maintenance_window(self, value: str):
        return self._add_property_field(self.__PROPERTY_PREFERRED_MAINTENANCE_WINDOW, value)

    def replication_source_identifier(self, value: str):
        return self._add_property_field(self.__PROPERTY_REPLICATION_SOURCE_IDENTIFIER, value)

    def restore_type(self, value: str):
        return self._add_property_field(self.__PROPERTY_RESTORE_TYPE, value)

    def scaling_configuration(self, value: ScalingConfiguration):
        return self._add_property_field(self.__PROPERTY_SCALING_CONFIGURATION, value.create())

    def snapshot_identifier(self, value: str):
        return self._add_property_field(self.__PROPERTY_SNAPSHOT_IDENTIFIER, value)

    def source_db_cluster_identifier(self, value: str):
        return self._add_property_field(self.__PROPERTY_SOURCE_DB_CLUSTER_IDENTIFIER, value)

    def source_region(self, value: str):
        return self._add_property_field(self.__PROPERTY_SOURCE_REGION, value)

    def storage_encrypted(self, value: bool):
        return self._add_property_field(self.__PROPERTY_STORAGE_ENCRYPTED, value)

    def tags(self, value: List[Tag]):
        return self._add_property_field(self.__PROPERTY_TAGS, [
            tag.create() for tag in value
        ])

    def use_latest_restorable_time(self, value: bool):
        return self._add_property_field(self.__PROPERTY_USE_LATEST_RESTORABLE_TIME, value)

    def vpc_security_group_ids(self, value: List[str]):
        return self._add_property_field(self.__PROPERTY_VPC_SECURITY_GROUP_IDS, value)
