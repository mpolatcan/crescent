from crescent.core import Resource, Tag, AllowedValues as CoreAllowedValues
from crescent.functions import AnyFn
from .db_instance_role import DBInstanceRole
from .processor_feature import ProcessorFeature
from .constants import AllowedValues, Conditions, ResourceRequiredProperties
from typing import Union


class DBInstance(Resource):
    __TYPE = "AWS::RDS::DBInstance"

    def __init__(self, id: str):
        super(DBInstance, self).__init__(
            id=id,
            type=self.__TYPE,
            min_value={self.AllocatedStorage.__name__: 100,
                       self.Iops.__name__: 1000,
                       self.PerformanceInsightsRetentionPeriod.__name__: 7,
                       self.PromotionTier.__name__: 0},
            max_value={self.PerformanceInsightsRetentionPeriod.__name__: 731,
                       self.PromotionTier.__name__: 15},
            pattern={self.MonitoringRoleArn.__name__: r"arn:.*"},
            allowed_values={self.AvailabilityZone.__name__: CoreAllowedValues.ZONE,
                            self.DBInstanceClass.__name__: AllowedValues.DB_INSTANCE_CLASS,
                            self.Engine.__name__: AllowedValues.ENGINE,
                            self.MonitoringInterval.__name__: AllowedValues.MONITORING_INTERVAL,
                            self.SourceRegion.__name__: CoreAllowedValues.REGION,
                            self.StorageType.__name__: AllowedValues.STORAGE_TYPE},
            conditions={self.BackupRetentionPeriod.__name__: Conditions.BACKUP_RETENTION_PERIOD,
                        self.CharacterSetName.__name__: Conditions.CHARACTER_SET_NAME,
                        self.CopyTagsToSnapshot.__name__: Conditions.COPY_TAGS_TO_SNAPSHOT,
                        self.DBName.__name__: Conditions.DB_NAME,
                        self.DeletionProtection.__name__: Conditions.DELETION_PROTECTION,
                        self.EnableIAMDatabaseAuthentication.__name__: Conditions.ENABLE_IAM_DATABASE_AUTHENTICATION,
                        self.EngineVersion.__name__: Conditions.ENGINE_VERSION,
                        self.MasterUserPassword.__name__: Conditions.MASTER_USER_PASSWORD,
                        self.StorageEncrypted.__name__: Conditions.STORAGE_ENCRYPTED},
            required_properties=ResourceRequiredProperties.DB_INSTANCE
        )

    def AllocatedStorage(self, allocated_storage: Union[int, AnyFn]):
        return self._set_property(self.AllocatedStorage.__name__, allocated_storage)

    def AllowMajorVersionUpgrade(self, allow_major_version_upgrade: Union[bool, AnyFn]):
        return self._set_property(self.AllowMajorVersionUpgrade.__name__, allow_major_version_upgrade)

    def AssociatedRoles(self, *associated_roles: DBInstanceRole):
        return self._set_property(self.AssociatedRoles.__name__, list(associated_roles))

    def AutoMinorVersionUpgrade(self, auto_minor_version_upgrade: Union[bool, AnyFn]):
        return self._set_property(self.AutoMinorVersionUpgrade.__name__, auto_minor_version_upgrade)

    def AvailabilityZone(self, availability_zone: Union[str, AnyFn]):
        return self._set_property(self.AvailabilityZone.__name__, availability_zone)

    def BackupRetentionPeriod(self, backup_retention_period: Union[int, AnyFn]):
        return self._set_property(self.BackupRetentionPeriod.__name__, backup_retention_period)

    def CACertificateIdentifier(self, ca_certificate_identifier: Union[str, AnyFn]):
        return self._set_property(self.CACertificateIdentifier.__name__, ca_certificate_identifier)

    def CharacterSetName(self, character_set_name: Union[str, AnyFn]):
        return self._set_property(self.CharacterSetName.__name__, character_set_name)

    def CopyTagsToSnapshot(self, copy_tags_to_snapshot: Union[bool, AnyFn]):
        return self._set_property(self.CopyTagsToSnapshot.__name__, copy_tags_to_snapshot)

    def DBClusterIdentifier(self, db_cluster_identifier: Union[str, AnyFn]):
        return self._set_property(self.DBClusterIdentifier.__name__, db_cluster_identifier)

    def DBInstanceClass(self, db_instance_class: Union[str, AnyFn]):
        return self._set_property(self.DBInstanceClass.__name__, db_instance_class)

    def DBInstanceIdentifier(self, db_instance_identifier: Union[str, AnyFn]):
        return self._set_property(self.DBInstanceIdentifier.__name__, db_instance_identifier)

    def DBName(self, db_name: Union[str, AnyFn]):
        return self._set_property(self.DBName.__name__, db_name)

    def DBParameterGroupName(self, db_parameter_group_name: Union[str, AnyFn]):
        return self._set_property(self.DBParameterGroupName.__name__, db_parameter_group_name)

    def DBSecurityGroups(self, *db_security_groups: Union[str, AnyFn]):
        return self._set_property(self.DBSecurityGroups.__name__, list(db_security_groups))

    def DBSnapshotIdentifier(self, db_snapshot_identifier: Union[str, AnyFn]):
        return self._set_property(self.DBSnapshotIdentifier.__name__, db_snapshot_identifier)

    def DBSubnetGroupName(self, db_subnet_group_name: Union[str, AnyFn]):
        return self._set_property(self.DBSubnetGroupName.__name__, db_subnet_group_name)

    def DeleteAutomatedBackups(self, delete_automated_backups: Union[bool, AnyFn]):
        return self._set_property(self.DeleteAutomatedBackups.__name__, delete_automated_backups)

    def DeletionProtection(self, deletion_protection: Union[bool, AnyFn]):
        return self._set_property(self.DeletionProtection.__name__, deletion_protection)

    def Domain(self, domain: Union[str, AnyFn]):
        return self._set_property(self.Domain.__name__, domain)

    def DomainIAMRoleName(self, domain_iam_role_name: Union[str, AnyFn]):
        return self._set_property(self.DomainIAMRoleName.__name__, domain_iam_role_name)

    def EnableCloudwatchLogsExports(self, *enable_cw_logs_exports: Union[str, AnyFn]):
        return self._set_property(self.EnableCloudwatchLogsExports.__name__, list(enable_cw_logs_exports))

    def EnableIAMDatabaseAuthentication(self, enable_iam_db_auth: Union[bool, AnyFn]):
        return self._set_property(self.EnableIAMDatabaseAuthentication.__name__, enable_iam_db_auth)

    def EnablePerformanceInsights(self, enable_performance_insights: Union[bool, AnyFn]):
        return self._set_property(self.EnablePerformanceInsights.__name__, enable_performance_insights)

    def Engine(self, engine: Union[str, AnyFn]):
        return self._set_property(self.Engine.__name__, engine)

    def EngineVersion(self, engine_version: Union[str, AnyFn]):
        return self._set_property(self.EngineVersion.__name__, engine_version)

    def Iops(self, iops: Union[int, AnyFn]):
        return self._set_property(self.Iops.__name__, iops)

    def KmsKeyId(self, kms_key_id: Union[str, AnyFn]):
        return self._set_property(self.KmsKeyId.__name__, kms_key_id)

    def LicenseModel(self, license_model: Union[str, AnyFn]):
        return self._set_property(self.LicenseModel.__name__, license_model)

    def MasterUsername(self, master_username: Union[str, AnyFn]):
        return self._set_property(self.MasterUsername.__name__, master_username)

    def MasterUserPassword(self, master_user_password: Union[str, AnyFn]):
        return self._set_property(self.MasterUserPassword.__name__, master_user_password)

    def MaxAllocatedStorage(self, max_allocated_storage: Union[int, AnyFn]):
        return self._set_property(self.MaxAllocatedStorage.__name__, max_allocated_storage)

    def MonitoringInterval(self, monitoring_interval: Union[int, AnyFn]):
        return self._set_property(self.MonitoringInterval.__name__, monitoring_interval)

    def MonitoringRoleArn(self, monitoring_role_arn: Union[str, AnyFn]):
        return self._set_property(self.MonitoringRoleArn.__name__, monitoring_role_arn)

    def MultiAz(self, multi_az: Union[bool, AnyFn]):
        return self._set_property(self.MultiAz.__name__, multi_az)

    def OptionGroupName(self, option_group_name: Union[str, AnyFn]):
        return self._set_property(self.OptionGroupName.__name__, option_group_name)

    def PerformanceInsightsKMSKeyId(self, performance_insights_kms_key_id: Union[str, AnyFn]):
        return self._set_property(self.PerformanceInsightsKMSKeyId.__name__, performance_insights_kms_key_id)

    def PerformanceInsightsRetentionPeriod(self, performance_insights_retention_period: Union[int, AnyFn]):
        return self._set_property(self.PerformanceInsightsRetentionPeriod.__name__, performance_insights_retention_period)

    def Port(self, port: Union[str, AnyFn]):
        return self._set_property(self.Port.__name__, port)

    def PreferredBackupWindow(self, preferred_backup_window: Union[str, AnyFn]):
        return self._set_property(self.PreferredBackupWindow.__name__, preferred_backup_window)

    def PreferredMaintenanceWindow(self, preferred_maintenance_window: Union[str, AnyFn]):
        return self._set_property(self.PreferredMaintenanceWindow.__name__, preferred_maintenance_window)

    def ProcessorFeatures(self, *processor_features: ProcessorFeature):
        return self._set_property(self.ProcessorFeatures.__name__, list(processor_features))

    def PromotionTier(self, promotion_tier: Union[int, AnyFn]):
        return self._set_property(self.PromotionTier.__name__, promotion_tier)

    def PubliclyAccessible(self, publicly_accessible: Union[bool, AnyFn]):
        return self._set_property(self.PubliclyAccessible.__name__, publicly_accessible)

    def SourceDBInstanceIdentifier(self, source_db_instance_identifier: Union[str, AnyFn]):
        return self._set_property(self.SourceDBInstanceIdentifier.__name__, source_db_instance_identifier)

    def SourceRegion(self, source_region: Union[str, AnyFn]):
        return self._set_property(self.SourceRegion.__name__, source_region)

    def StorageEncrypted(self, storage_encrypted: Union[bool, AnyFn]):
        return self._set_property(self.StorageEncrypted.__name__, storage_encrypted)

    def StorageType(self, storage_type: Union[str, AnyFn]):
        return self._set_property(self.StorageType.__name__, storage_type)

    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))

    def Timezone(self, timezone: Union[str, AnyFn]):
        return self._set_property(self.Timezone.__name__, timezone)

    def UseDefaultProcessorFeatures(self, use_default_processor_features: Union[bool, AnyFn]):
        return self._set_property(self.UseDefaultProcessorFeatures.__name__, use_default_processor_features)

    def VPCSecurityGroups(self, *vpc_security_groups: Union[str, AnyFn]):
        return self._set_property(self.VPCSecurityGroups.__name__, list(vpc_security_groups))

