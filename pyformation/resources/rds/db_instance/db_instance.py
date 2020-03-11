from pyformation.resources.shared import BaseCloudFormationResourceModel, Tag
from pyformation.resources.rds.db_instance import DBInstanceRole, ProcessorFeature


class DBInstance(BaseCloudFormationResourceModel):
    __TYPE = "AWS::RDS::DBInstance"
    __PROPERTY_ALLOCATED_STORAGE = "AllocatedStorage"
    __PROPERTY_ALLOW_MAJOR_VERSION_UPGRADE = "AllowMajorVersionUpgrade"
    __PROPERTY_ASSOCIATED_ROLES = "AssociatedRoles"
    __PROPERTY_AUTO_MINOR_VERSION_UPGRADE = "AutoMinorVersionUpgrade"
    __PROPERTY_AVAILABILITY_ZONE = "AvailabilityZone"
    __PROPERTY_BACKUP_RETENTION_PERIOD = "BackupRetentionPeriod"
    __PROPERTY_CA_CERTIFICATE_IDENTIFIER = "CACertificateIdentifier"
    __PROPERTY_CHARACTER_SET_NAME = "CharacterSetName"
    __PROPERTY_COPY_TAGS_TO_SNAPSHOT = "CopyTagsToSnapshot"
    __PROPERTY_DB_CLUSTER_IDENTIFIER = "DBClusterIdentifier"
    __PROPERTY_DB_INSTANCE_CLASS = "DBInstanceClass"
    __PROPERTY_DB_INSTANCE_IDENTIFIER = "DBInstanceIdentifier"
    __PROPERTY_DB_NAME = "DBName"
    __PROPERTY_DB_PARAMETER_GROUP_NAME = "DBParameterGroupName"
    __PROPERTY_DB_SECURITY_GROUPS = "DBSecurityGroups"
    __PROPERTY_DB_SNAPSHOT_IDENTIFIER = "DBSnapshotIdentifier"
    __PROPERTY_DB_SUBNET_GROUP_NAME = "DBSubnetGroupName"
    __PROPERTY_DELETE_AUTOMATED_BACKUPS = "DeleteAutomatedBackups"
    __PROPERTY_DELETION_PROTECTION = "DeletionProtection"
    __PROPERTY_DOMAIN = "Domain"
    __PROPERTY_DOMAIN_IAM_ROLE_NAME = "DomainIAMRoleName"
    __PROPERTY_ENABLE_CLOUDWATCH_LOGS_EXPORTS = "EnableCloudwatchLogsExports"
    __PROPERTY_ENABLE_IAM_DATABASE_AUTHENTICATION = "EnableIAMDatabaseAuthentication"
    __PROPERTY_ENABLE_PERFORMANCE_INSIGHTS = "EnablePerformanceInsights"
    __PROPERTY_ENGINE = "Engine"
    __PROPERTY_ENGINE_VERSION = "EngineVersion"
    __PROPERTY_IOPS = "Iops"
    __PROPERTY_KMS_KEY_ID = "KmsKeyId"
    __PROPERTY_LICENSE_MODEL = "LicenseModel"
    __PROPERTY_MASTER_USERNAME = "MasterUsername"
    __PROPERTY_MASTER_USER_PASSWORD = "MasterUserPassword"
    __PROPERTY_MAX_ALLOCATED_STORAGE = "MaxAllocatedStorage"
    __PROPERTY_MONITORING_INTERVAL = "MonitoringInterval"
    __PROPERTY_MONITORING_ROLE_ARN = "MonitoringRoleArn"
    __PROPERTY_MULTI_AZ = "MultiAz"
    __PROPERTY_OPTION_GROUP_NAME = "OptionGroupName"
    __PROPERTY_PERFORMANCE_INSIGHTS_KMS_KEY_ID = "PerformanceInsightsKMSKeyId"
    __PROPERTY_PERFORMANCE_INSIGHTS_RETENTION_PERIOD = "PerformanceInsightsRetentionPeriod"
    __PROPERTY_PORT = "Port"
    __PROPERTY_PREFERRED_BACKUP_WINDOW = "PreferredBackupWindow"
    __PROPERTY_PREFERRED_MAINTENANCE_WINDOW = "PreferredMaintenanceWindow"
    __PROPERTY_PROCESSOR_FEATURES = "ProcessorFeatures"
    __PROPERTY_PROMOTION_TIER = "PromotionTier"
    __PROPERTY_PUBLICLY_ACCESSIBLE = "PubliclyAccessible"
    __PROPERTY_SOURCE_DB_INSTANCE_IDENTIFIER = "SourceDBInstanceIdentifier"
    __PROPERTY_SOURCE_REGION = "SourceRegion"
    __PROPERTY_STORAGE_ENCRYPTED = "StorageEncrypted"
    __PROPERTY_STORAGE_TYPE = "StorageType"
    __PROPERTY_TAGS = "Tags"
    __PROPERTY_TIMEZONE = "Timezone"
    __PROPERTY_USE_DEFAULT_PROCESSOR_FEATURES = "UseDefaultProcessorFeatures"
    __PROPERTY_VPC_SECURITY_GROUPS = "VPCSecurityGroups"

    def __init__(self):
        super(DBInstance, self).__init__(type=self.__TYPE)

    def allocated_storage(self, value: str):
        return self._add_property_field(self.__PROPERTY_ALLOCATED_STORAGE, value)

    def allow_major_version_upgrade(self, value: bool):
        return self._add_property_field(self.__PROPERTY_ALLOW_MAJOR_VERSION_UPGRADE, value)

    def associated_roles(self, *value: DBInstanceRole):
        return self._add_property_field(self.__PROPERTY_ASSOCIATED_ROLES, [
            db_instance_role.create() for db_instance_role in list(value)
        ])

    def auto_minor_version_upgrade(self, value: bool):
        return self._add_property_field(self.__PROPERTY_AUTO_MINOR_VERSION_UPGRADE, value)

    def availability_zone(self, value: str):
        return self._add_property_field(self.__PROPERTY_AVAILABILITY_ZONE, value)

    def backup_retention_period(self, value: int):
        return self._add_property_field(self.__PROPERTY_BACKUP_RETENTION_PERIOD, value)

    def ca_certificate_identifier(self, value: str):
        return self._add_property_field(self.__PROPERTY_CA_CERTIFICATE_IDENTIFIER, value)

    def character_set_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_CHARACTER_SET_NAME, value)

    def copy_tags_to_snapshot(self, value: bool):
        return self._add_property_field(self.__PROPERTY_COPY_TAGS_TO_SNAPSHOT, value)

    def db_cluster_identifier(self, value: str):
        return self._add_property_field(self.__PROPERTY_DB_CLUSTER_IDENTIFIER, value)

    def db_instance_class(self, value: str):
        return self._add_property_field(self.__PROPERTY_DB_INSTANCE_CLASS, value)

    def db_instance_class_identifier(self, value: str):
        return self._add_property_field(self.__PROPERTY_DB_INSTANCE_CLASS, value)

    def db_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_DB_NAME, value)

    def db_parameter_group_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_DB_PARAMETER_GROUP_NAME, value)

    def db_security_groups(self, *value: str):
        return self._add_property_field(self.__PROPERTY_DB_SECURITY_GROUPS, list(value))

    def db_snapshot_identifier(self, value: str):
        return self._add_property_field(self.__PROPERTY_DB_SNAPSHOT_IDENTIFIER, value)

    def db_subnet_group_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_DB_SUBNET_GROUP_NAME, value)

    def delete_automated_backups(self, value: bool):
        return self._add_property_field(self.__PROPERTY_DELETE_AUTOMATED_BACKUPS, value)

    def deletion_protection(self, value: bool):
        return self._add_property_field(self.__PROPERTY_DELETION_PROTECTION, value)

    def domain(self, value: str):
        return self._add_property_field(self.__PROPERTY_DOMAIN, value)

    def domain_iam_role_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_DOMAIN_IAM_ROLE_NAME, value)

    def enable_cloudwatch_logs_exports(self, *value: str):
        return self._add_property_field(self.__PROPERTY_ENABLE_CLOUDWATCH_LOGS_EXPORTS, list(value))

    def enable_iam_database_authentication(self, value: bool):
        return self._add_property_field(self.__PROPERTY_ENABLE_IAM_DATABASE_AUTHENTICATION, value)

    def enable_performance_insights(self, value: bool):
        return self._add_property_field(self.__PROPERTY_ENABLE_PERFORMANCE_INSIGHTS, value)

    def engine(self, value: str):
        return self._add_property_field(self.__PROPERTY_ENGINE, value)

    def engine_version(self, value: str):
        return self._add_property_field(self.__PROPERTY_ENGINE_VERSION, value)

    def iops(self, value: int):
        return self._add_property_field(self.__PROPERTY_IOPS, value)

    def kms_key_id(self, value: str):
        return self._add_property_field(self.__PROPERTY_KMS_KEY_ID, value)

    def license_model(self, value: str):
        return self._add_property_field(self.__PROPERTY_LICENSE_MODEL, value)

    def master_username(self, value: str):
        return self._add_property_field(self.__PROPERTY_MASTER_USERNAME, value)

    def master_user_password(self, value: str):
        return self._add_property_field(self.__PROPERTY_MASTER_USER_PASSWORD, value)

    def max_allocated_storage(self, value: int):
        return self._add_property_field(self.__PROPERTY_MAX_ALLOCATED_STORAGE, value)

    def monitoring_interval(self, value: int):
        return self._add_property_field(self.__PROPERTY_MONITORING_INTERVAL, value)

    def monitoring_role_arn(self, value: str):
        return self._add_property_field(self.__PROPERTY_MONITORING_ROLE_ARN, value)

    def multi_az(self, value: bool):
        return self._add_property_field(self.__PROPERTY_MULTI_AZ, value)

    def option_group_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_OPTION_GROUP_NAME, value)

    def performance_insights_kms_key_id(self, value: str):
        return self._add_property_field(self.__PROPERTY_PERFORMANCE_INSIGHTS_KMS_KEY_ID, value)

    def performance_insights_retention_period(self, value: int):
        return self._add_property_field(self.__PROPERTY_PERFORMANCE_INSIGHTS_RETENTION_PERIOD, value)

    def port(self, value: str):
        return self._add_property_field(self.__PROPERTY_PORT, value)

    def preferred_backup_window(self, value: str):
        return self._add_property_field(self.__PROPERTY_PREFERRED_BACKUP_WINDOW, value)

    def preferred_maintenance_window(self, value: str):
        return self._add_property_field(self.__PROPERTY_PREFERRED_MAINTENANCE_WINDOW, value)

    def processor_features(self, *value: ProcessorFeature):
        return self._add_property_field(self.__PROPERTY_PROCESSOR_FEATURES, [
            processor_feature.create() for processor_feature in list(value)
        ])

    def promotion_tier(self, value: int):
        return self._add_property_field(self.__PROPERTY_PROMOTION_TIER, value)

    def publicly_accessible(self, value: bool):
        return self._add_property_field(self.__PROPERTY_PUBLICLY_ACCESSIBLE, value)

    def source_db_instance_identifier(self, value: str):
        return self._add_property_field(self.__PROPERTY_SOURCE_DB_INSTANCE_IDENTIFIER, value)

    def source_region(self, value: str):
        return self._add_property_field(self.__PROPERTY_SOURCE_REGION, value)

    def storage_encrypted(self, value: bool):
        return self._add_property_field(self.__PROPERTY_STORAGE_ENCRYPTED, value)

    def storage_type(self, value: str):
        return self._add_property_field(self.__PROPERTY_STORAGE_TYPE, value)

    def tags(self, *value: Tag):
        return self._add_property_field(self.__PROPERTY_TAGS, [
            tag.create() for tag in list(value)
        ])

    def timezone(self, value: str):
        return self._add_property_field(self.__PROPERTY_TIMEZONE, value)

    def use_default_processor_features(self, value: bool):
        return self._add_property_field(self.__PROPERTY_USE_DEFAULT_PROCESSOR_FEATURES, value)

    def vpc_security_groups(self, *value: str):
        return self._add_property_field(self.__PROPERTY_VPC_SECURITY_GROUPS, list(value))
