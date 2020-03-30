from crescent.core import Resource, Tag, Validator, AllowedValues as CoreAllowedValues
from .db_instance_role import DBInstanceRole
from .processor_feature import ProcessorFeature
from .constants import AllowedValues, ModelRequiredProperties, Conditions


class DBInstance(Resource):
    __TYPE = "AWS::RDS::DBInstance"

    def __init__(self, id: str):
        super(DBInstance, self).__init__(id, self.__TYPE)

    @Validator.validate(type=int, min_value=100)
    def AllocatedStorage(self, allocated_storage: int):
        return self._set_property(self.AllocatedStorage.__name__, allocated_storage)

    @Validator.validate(type=bool)
    def AllowMajorVersionUpgrade(self, allow_major_version_upgrade: bool):
        return self._set_property(self.AllowMajorVersionUpgrade.__name__, allow_major_version_upgrade)

    @Validator.validate(type=DBInstanceRole, required_properties=ModelRequiredProperties.DB_INSTANCE_ROLE)
    def AssociatedRoles(self, *associated_roles: DBInstanceRole):
        return self._set_property(self.AssociatedRoles.__name__, [db_inst_role.__to_dict__() for db_inst_role in list(associated_roles)])

    @Validator.validate(type=bool)
    def AutoMinorVersionUpgrade(self, auto_minor_version_upgrade: bool):
        return self._set_property(self.AutoMinorVersionUpgrade.__name__, auto_minor_version_upgrade)

    @Validator.validate(type=str, allowed_values=CoreAllowedValues.ZONE)
    def AvailabilityZone(self, availability_zone: str):
        return self._set_property(self.AvailabilityZone.__name__, availability_zone)

    @Validator.validate(type=int, conditions=Conditions.BACKUP_RETENTION_PERIOD)
    def BackupRetentionPeriod(self, backup_retention_period: int):
        return self._set_property(self.BackupRetentionPeriod.__name__, backup_retention_period)

    @Validator.validate(type=str)
    def CACertificateIdentifier(self, ca_certificate_identifier: str):
        return self._set_property(self.CACertificateIdentifier.__name__, ca_certificate_identifier)

    @Validator.validate(type=str, conditions=Conditions.CHARACTER_SET_NAME)
    def CharacterSetName(self, character_set_name: str):
        return self._set_property(self.CharacterSetName.__name__, character_set_name)

    @Validator.validate(type=bool, conditions=Conditions.COPY_TAGS_TO_SNAPSHOT)
    def CopyTagsToSnapshot(self, copy_tags_to_snapshot: bool):
        return self._set_property(self.CopyTagsToSnapshot.__name__, copy_tags_to_snapshot)

    @Validator.validate(type=str)
    def DBClusterIdentifier(self, db_cluster_identifier: str):
        return self._set_property(self.DBClusterIdentifier.__name__, db_cluster_identifier)

    @Validator.validate(type=str, allowed_values=AllowedValues.DB_INSTANCE_CLASS)
    def DBInstanceClass(self, db_instance_class: str):
        return self._set_property(self.DBInstanceClass.__name__, db_instance_class)

    @Validator.validate(type=str)
    def DBInstanceIdentifier(self, db_instance_identifier: str):
        return self._set_property(self.DBInstanceIdentifier.__name__, db_instance_identifier)

    @Validator.validate(type=str, conditions=Conditions.DB_NAME)
    def DBName(self, db_name: str):
        return self._set_property(self.DBName.__name__, db_name)

    @Validator.validate(type=str)
    def DBParameterGroupName(self, db_parameter_group_name: str):
        return self._set_property(self.DBParameterGroupName.__name__, db_parameter_group_name)

    @Validator.validate(type=str)
    def DBSecurityGroups(self, *db_security_groups: str):
        return self._set_property(self.DBSecurityGroups.__name__, list(db_security_groups))

    @Validator.validate(type=str)
    def DBSnapshotIdentifier(self, db_snapshot_identifier: str):
        return self._set_property(self.DBSnapshotIdentifier.__name__, db_snapshot_identifier)

    @Validator.validate(type=str)
    def DBSubnetGroupName(self, db_subnet_group_name: str):
        return self._set_property(self.DBSubnetGroupName.__name__, db_subnet_group_name)

    @Validator.validate(type=bool)
    def DeleteAutomatedBackups(self, delete_automated_backups: bool):
        return self._set_property(self.DeleteAutomatedBackups.__name__, delete_automated_backups)

    @Validator.validate(type=bool, conditions=Conditions.DELETION_PROTECTION)
    def DeletionProtection(self, deletion_protection: bool):
        return self._set_property(self.DeletionProtection.__name__, deletion_protection)

    @Validator.validate(type=str)
    def Domain(self, domain: str):
        return self._set_property(self.Domain.__name__, domain)

    @Validator.validate(type=str)
    def DomainIAMRoleName(self, domain_iam_role_name: str):
        return self._set_property(self.DomainIAMRoleName.__name__, domain_iam_role_name)

    @Validator.validate(type=str)
    def EnableCloudwatchLogsExports(self, *enable_cw_logs_exports: str):
        return self._set_property(self.EnableCloudwatchLogsExports.__name__, list(enable_cw_logs_exports))

    @Validator.validate(type=bool, conditions=Conditions.ENABLE_IAM_DATABASE_AUTHENTICATION)
    def EnableIAMDatabaseAuthentication(self, enable_iam_db_auth: bool):
        return self._set_property(self.EnableIAMDatabaseAuthentication.__name__, enable_iam_db_auth)

    @Validator.validate(type=bool)
    def EnablePerformanceInsights(self, enable_performance_insights: bool):
        return self._set_property(self.EnablePerformanceInsights.__name__, enable_performance_insights)

    @Validator.validate(type=str, allowed_values=AllowedValues.ENGINE)
    def Engine(self, engine: str):
        return self._set_property(self.Engine.__name__, engine)

    @Validator.validate(type=str, conditions=Conditions.ENGINE_VERSION)
    def EngineVersion(self, engine_version: str):
        return self._set_property(self.EngineVersion.__name__, engine_version)

    @Validator.validate(type=int, min_value=1000)
    def Iops(self, iops: int):
        return self._set_property(self.Iops.__name__, iops)

    @Validator.validate(type=str)
    def KmsKeyId(self, kms_key_id: str):
        return self._set_property(self.KmsKeyId.__name__, kms_key_id)

    @Validator.validate(type=str)
    def LicenseModel(self, license_model: str):
        return self._set_property(self.LicenseModel.__name__, license_model)

    @Validator.validate(type=str)
    def MasterUsername(self, master_username: str):
        return self._set_property(self.MasterUsername.__name__, master_username)

    @Validator.validate(type=str, conditions=Conditions.MASTER_USER_PASSWORD)
    def MasterUserPassword(self, master_user_password: str):
        return self._set_property(self.MasterUserPassword.__name__, master_user_password)

    @Validator.validate(type=int)
    def MaxAllocatedStorage(self, max_allocated_storage: int):
        return self._set_property(self.MaxAllocatedStorage.__name__, max_allocated_storage)

    @Validator.validate(type=int, allowed_values=AllowedValues.MONITORING_INTERVAL)
    def MonitoringInterval(self, monitoring_interval: int):
        return self._set_property(self.MonitoringInterval.__name__, monitoring_interval)

    @Validator.validate(type=str, pattern=r"arn:.*")
    def MonitoringRoleArn(self, monitoring_role_arn: str):
        return self._set_property(self.MonitoringRoleArn.__name__, monitoring_role_arn)

    @Validator.validate(type=bool)
    def MultiAz(self, multi_az: bool):
        return self._set_property(self.MultiAz.__name__, multi_az)

    @Validator.validate(type=str)
    def OptionGroupName(self, option_group_name: str):
        return self._set_property(self.OptionGroupName.__name__, option_group_name)

    @Validator.validate(type=str)
    def PerformanceInsightsKMSKeyId(self, performance_insights_kms_key_id: str):
        return self._set_property(self.PerformanceInsightsKMSKeyId.__name__, performance_insights_kms_key_id)

    @Validator.validate(type=int, min_value=7, max_value=731)
    def PerformanceInsightsRetentionPeriod(self, performance_insights_retention_period: int):
        return self._set_property(self.PerformanceInsightsRetentionPeriod.__name__, performance_insights_retention_period)

    @Validator.validate(type=str)
    def Port(self, port: str):
        return self._set_property(self.Port.__name__, port)

    @Validator.validate(type=str)
    def PreferredBackupWindow(self, preferred_backup_window: str):
        return self._set_property(self.PreferredBackupWindow.__name__, preferred_backup_window)

    @Validator.validate(type=str)
    def PreferredMaintenanceWindow(self, preferred_maintenance_window: str):
        return self._set_property(self.PreferredMaintenanceWindow.__name__, preferred_maintenance_window)

    @Validator.validate(type=ProcessorFeature)
    def ProcessorFeatures(self, *processor_features: ProcessorFeature):
        return self._set_property(self.ProcessorFeatures.__name__, [pf.__to_dict__() for pf in list(processor_features)])

    @Validator.validate(type=int, min_value=0, max_value=15)
    def PromotionTier(self, promotion_tier: int):
        return self._set_property(self.PromotionTier.__name__, promotion_tier)

    @Validator.validate(type=bool)
    def PubliclyAccessible(self, publicly_accessible: bool):
        return self._set_property(self.PubliclyAccessible.__name__, publicly_accessible)

    @Validator.validate(type=str)
    def SourceDBInstanceIdentifier(self, source_db_instance_identifier: str):
        return self._set_property(self.SourceDBInstanceIdentifier.__name__, source_db_instance_identifier)

    @Validator.validate(type=str, allowed_values=CoreAllowedValues.REGION)
    def SourceRegion(self, source_region: str):
        return self._set_property(self.SourceRegion.__name__, source_region)

    @Validator.validate(type=bool, conditions=Conditions.STORAGE_ENCRYPTED)
    def StorageEncrypted(self, storage_encrypted: bool):
        return self._set_property(self.StorageEncrypted.__name__, storage_encrypted)

    @Validator.validate(type=str, allowed_values=AllowedValues.STORAGE_TYPE)
    def StorageType(self, storage_type: str):
        return self._set_property(self.StorageType.__name__, storage_type)

    @Validator.validate(type=Tag)
    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))

    @Validator.validate(type=str)
    def Timezone(self, timezone: str):
        return self._set_property(self.Timezone.__name__, timezone)

    @Validator.validate(type=bool)
    def UseDefaultProcessorFeatures(self, use_default_processor_features: bool):
        return self._set_property(self.UseDefaultProcessorFeatures.__name__, use_default_processor_features)

    @Validator.validate(type=str)
    def VPCSecurityGroups(self, *vpc_security_groups: str):
        return self._set_property(self.VPCSecurityGroups.__name__, list(vpc_security_groups))

