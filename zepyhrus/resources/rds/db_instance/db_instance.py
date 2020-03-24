from zepyhrus.core import Resource, Tag, Validator
from .db_instance_role import DBInstanceRole
from .processor_feature import ProcessorFeature
from .constants import RequiredProperties


class DBInstance(Resource):
    __TYPE = "AWS::RDS::DBInstance"

    def __init__(self, id: str):
        super(DBInstance, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def AllocatedStorage(self, value: str):
        return self._set_property(self.AllocatedStorage.__name__, value)

    @Validator.validate(type=bool)
    def AllowMajorVersionUpgrade(self, value: bool):
        return self._set_property(self.AllowMajorVersionUpgrade.__name__, value)

    @Validator.validate(type=DBInstanceRole, required_properties=RequiredProperties.DB_INSTANCE_ROLE)
    def AssociatedRoles(self, *value: DBInstanceRole):
        return self._set_property(self.AssociatedRoles.__name__, [db_inst_role.__to_dict__() for db_inst_role in list(value)])

    @Validator.validate(type=bool)
    def AutoMinorVersionUpgrade(self, value: bool):
        return self._set_property(self.AutoMinorVersionUpgrade.__name__, value)

    @Validator.validate(type=str)
    def AvailabilityZone(self, value: str):
        return self._set_property(self.AvailabilityZone.__name__, value)

    @Validator.validate(type=int)
    def BackupRetentionPeriod(self, value: int):
        return self._set_property(self.BackupRetentionPeriod.__name__, value)

    @Validator.validate(type=str)
    def CACertificateIdentifier(self, value: str):
        return self._set_property(self.CACertificateIdentifier.__name__, value)

    @Validator.validate(type=str)
    def CharacterSetName(self, value: str):
        return self._set_property(self.CharacterSetName.__name__, value)

    @Validator.validate(type=bool)
    def CopyTagsToSnapshot(self, value: bool):
        return self._set_property(self.CopyTagsToSnapshot.__name__, value)

    @Validator.validate(type=str)
    def DBClusterIdentifier(self, value: str):
        return self._set_property(self.DBClusterIdentifier.__name__, value)

    @Validator.validate(type=str)
    def DBInstanceClass(self, value: str):
        return self._set_property(self.DBInstanceClass.__name__, value)

    @Validator.validate(type=str)
    def DBInstanceIdentifier(self, value: str):
        return self._set_property(self.DBInstanceIdentifier.__name__, value)

    @Validator.validate(type=str)
    def DBName(self, value: str):
        return self._set_property(self.DBName.__name__, value)

    @Validator.validate(type=str)
    def DBParameterGroupName(self, value: str):
        return self._set_property(self.DBParameterGroupName.__name__, value)

    @Validator.validate(type=str)
    def DBSecurityGroups(self, *value: str):
        return self._set_property(self.DBSecurityGroups.__name__, list(value))

    @Validator.validate(type=str)
    def DBSnapshotIdentifier(self, value: str):
        return self._set_property(self.DBSnapshotIdentifier.__name__, value)

    @Validator.validate(type=str)
    def DBSubnetGroupName(self, value: str):
        return self._set_property(self.DBSubnetGroupName.__name__, value)

    @Validator.validate(type=bool)
    def DeleteAutomatedBackups(self, value: bool):
        return self._set_property(self.DeleteAutomatedBackups.__name__, value)

    @Validator.validate(type=bool)
    def DeletionProtection(self, value: bool):
        return self._set_property(self.DeletionProtection.__name__, value)

    @Validator.validate(type=str)
    def Domain(self, value: str):
        return self._set_property(self.Domain.__name__, value)

    @Validator.validate(type=str)
    def DomainIAMRoleName(self, value: str):
        return self._set_property(self.DomainIAMRoleName.__name__, value)

    @Validator.validate(type=str)
    def EnableCloudwatchLogsExports(self, *value: str):
        return self._set_property(self.EnableCloudwatchLogsExports.__name__, list(value))

    @Validator.validate(type=bool)
    def EnableIAMDatabaseAuthentication(self, value: bool):
        return self._set_property(self.EnableIAMDatabaseAuthentication.__name__, value)

    @Validator.validate(type=bool)
    def EnablePerformanceInsights(self, value: bool):
        return self._set_property(self.EnablePerformanceInsights.__name__, value)

    @Validator.validate(type=str)
    def Engine(self, value: str):
        return self._set_property(self.Engine.__name__, value)

    @Validator.validate(type=str)
    def EngineVersion(self, value: str):
        return self._set_property(self.EngineVersion.__name__, value)

    @Validator.validate(type=int)
    def Iops(self, value: int):
        return self._set_property(self.Iops.__name__, value)

    @Validator.validate(type=str)
    def KmsKeyId(self, value: str):
        return self._set_property(self.KmsKeyId.__name__, value)

    @Validator.validate(type=str)
    def LicenseModel(self, value: str):
        return self._set_property(self.LicenseModel.__name__, value)

    @Validator.validate(type=str)
    def MasterUsername(self, value: str):
        return self._set_property(self.MasterUsername.__name__, value)

    @Validator.validate(type=str)
    def MasterUserPassword(self, value: str):
        return self._set_property(self.MasterUserPassword.__name__, value)

    @Validator.validate(type=int)
    def MaxAllocatedStorage(self, value: int):
        return self._set_property(self.MaxAllocatedStorage.__name__, value)

    @Validator.validate(type=int)
    def MonitoringInterval(self, value: int):
        return self._set_property(self.MonitoringInterval.__name__, value)

    @Validator.validate(type=str)
    def MonitoringRoleArn(self, value: str):
        return self._set_property(self.MonitoringRoleArn.__name__, value)

    @Validator.validate(type=bool)
    def MultiAz(self, value: bool):
        return self._set_property(self.MultiAz.__name__, value)

    @Validator.validate(type=str)
    def OptionGroupName(self, value: str):
        return self._set_property(self.OptionGroupName.__name__, value)

    @Validator.validate(type=str)
    def PerformanceInsightsKMSKeyId(self, value: str):
        return self._set_property(self.PerformanceInsightsKMSKeyId.__name__, value)

    @Validator.validate(type=int)
    def PerformanceInsightsRetentionPeriod(self, value: int):
        return self._set_property(self.PerformanceInsightsRetentionPeriod.__name__, value)

    @Validator.validate(type=str)
    def Port(self, value: str):
        return self._set_property(self.Port.__name__, value)

    @Validator.validate(type=str)
    def PreferredBackupWindow(self, value: str):
        return self._set_property(self.PreferredBackupWindow.__name__, value)

    @Validator.validate(type=str)
    def PreferredMaintenanceWindow(self, value: str):
        return self._set_property(self.PreferredMaintenanceWindow.__name__, value)

    @Validator.validate(type=ProcessorFeature)
    def ProcessorFeatures(self, *value: ProcessorFeature):
        return self._set_property(self.ProcessorFeatures.__name__, [pf.__to_dict__() for pf in list(value)])

    @Validator.validate(type=int)
    def PromotionTier(self, value: int):
        return self._set_property(self.PromotionTier.__name__, value)

    @Validator.validate(type=bool)
    def PubliclyAccessible(self, value: bool):
        return self._set_property(self.PubliclyAccessible.__name__, value)

    @Validator.validate(type=str)
    def SourceDBInstanceIdentifier(self, value: str):
        return self._set_property(self.SourceDBInstanceIdentifier.__name__, value)

    @Validator.validate(type=str)
    def SourceRegion(self, value: str):
        return self._set_property(self.SourceRegion.__name__, value)

    @Validator.validate(type=bool)
    def StorageEncrypted(self, value: bool):
        return self._set_property(self.StorageEncrypted.__name__, value)

    @Validator.validate(type=str)
    def StorageType(self, value: str):
        return self._set_property(self.StorageType.__name__, value)

    @Validator.validate(type=Tag)
    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))

    @Validator.validate(type=str)
    def Timezone(self, value: str):
        return self._set_property(self.Timezone.__name__, value)

    @Validator.validate(type=bool)
    def UseDefaultProcessorFeatures(self, value: bool):
        return self._set_property(self.UseDefaultProcessorFeatures.__name__, value)

    @Validator.validate(type=str)
    def VPCSecurityGroups(self, *value: str):
        return self._set_property(self.VPCSecurityGroups.__name__, list(value))

