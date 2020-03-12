from pyformation import PyformationResource, Tag
from .db_instance_role import DBInstanceRole
from .processor_feature import ProcessorFeature


class DBInstance(PyformationResource):
    __TYPE = "AWS::RDS::DBInstance"

    def __init__(self, id: str):
        super(DBInstance, self).__init__(id, self.__TYPE)

    def AllocatedStorage(self, value: str):
        return self._set_property(self.AllocatedStorage.__name__, value)

    def AllowMajorVersionUpgrade(self, value: bool):
        return self._set_property(self.AllowMajorVersionUpgrade.__name__, value)

    def AssociatedRoles(self, *value: DBInstanceRole):
        return self._set_property(self.AssociatedRoles.__name__, [db_inst_role.__to_dict__() for db_inst_role in list(value)])

    def AutoMinorVersionUpgrade(self, value: bool):
        return self._set_property(self.AutoMinorVersionUpgrade.__name__, value)

    def AvailabilityZone(self, value: str):
        return self._set_property(self.AvailabilityZone.__name__, value)

    def BackupRetentionPeriod(self, value: int):
        return self._set_property(self.BackupRetentionPeriod.__name__, value)

    def CACertificateIdentifier(self, value: str):
        return self._set_property(self.CACertificateIdentifier.__name__, value)

    def CharacterSetName(self, value: str):
        return self._set_property(self.CharacterSetName.__name__, value)

    def CopyTagsToSnapshot(self, value: bool):
        return self._set_property(self.CopyTagsToSnapshot.__name__, value)

    def DBClusterIdentifier(self, value: str):
        return self._set_property(self.DBClusterIdentifier.__name__, value)

    def DBInstanceClass(self, value: str):
        return self._set_property(self.DBInstanceClass.__name__, value)

    def DBInstanceIdentifier(self, value: str):
        return self._set_property(self.DBInstanceIdentifier.__name__, value)

    def DBName(self, value: str):
        return self._set_property(self.DBName.__name__, value)

    def DBParameterGroupName(self, value: str):
        return self._set_property(self.DBParameterGroupName.__name__, value)

    def DBSecurityGroups(self, *value: str):
        return self._set_property(self.DBSecurityGroups.__name__, list(value))

    def DBSnapshotIdentifier(self, value: str):
        return self._set_property(self.DBSnapshotIdentifier.__name__, value)

    def DBSubnetGroupName(self, value: str):
        return self._set_property(self.DBSubnetGroupName.__name__, value)

    def DeleteAutomatedBackups(self, value: bool):
        return self._set_property(self.DeleteAutomatedBackups.__name__, value)

    def DeletionProtection(self, value: bool):
        return self._set_property(self.DeletionProtection.__name__, value)

    def Domain(self, value: str):
        return self._set_property(self.Domain.__name__, value)

    def DomainIAMRoleName(self, value: str):
        return self._set_property(self.DomainIAMRoleName.__name__, value)

    def EnableCloudwatchLogsExports(self, *value: str):
        return self._set_property(self.EnableCloudwatchLogsExports.__name__, list(value))

    def EnableIAMDatabaseAuthentication(self, value: bool):
        return self._set_property(self.EnableIAMDatabaseAuthentication.__name__, value)

    def EnablePerformanceInsights(self, value: bool):
        return self._set_property(self.EnablePerformanceInsights.__name__, value)

    def Engine(self, value: str):
        return self._set_property(self.Engine.__name__, value)

    def EngineVersion(self, value: str):
        return self._set_property(self.EngineVersion.__name__, value)

    def Iops(self, value: int):
        return self._set_property(self.Iops.__name__, value)

    def KmsKeyId(self, value: str):
        return self._set_property(self.KmsKeyId.__name__, value)

    def LicenseModel(self, value: str):
        return self._set_property(self.LicenseModel.__name__, value)

    def MasterUsername(self, value: str):
        return self._set_property(self.MasterUsername.__name__, value)

    def MasterUserPassword(self, value: str):
        return self._set_property(self.MasterUserPassword.__name__, value)

    def MaxAllocatedStorage(self, value: int):
        return self._set_property(self.MaxAllocatedStorage.__name__, value)

    def MonitoringInterval(self, value: int):
        return self._set_property(self.MonitoringInterval.__name__, value)

    def MonitoringRoleArn(self, value: str):
        return self._set_property(self.MonitoringRoleArn.__name__, value)

    def MultiAz(self, value: bool):
        return self._set_property(self.MultiAz.__name__, value)

    def OptionGroupName(self, value: str):
        return self._set_property(self.OptionGroupName.__name__, value)

    def PerformanceInsightsKMSKeyId(self, value: str):
        return self._set_property(self.PerformanceInsightsKMSKeyId.__name__, value)

    def PerformanceInsightsRetentionPeriod(self, value: int):
        return self._set_property(self.PerformanceInsightsRetentionPeriod.__name__, value)

    def Port(self, value: str):
        return self._set_property(self.Port.__name__, value)

    def PreferredBackupWindow(self, value: str):
        return self._set_property(self.PreferredBackupWindow.__name__, value)

    def PreferredMaintenanceWindow(self, value: str):
        return self._set_property(self.PreferredMaintenanceWindow.__name__, value)

    def ProcessorFeatures(self, *value: ProcessorFeature):
        return self._set_property(self.ProcessorFeatures.__name__, [pf.__to_dict__() for pf in list(value)])

    def PromotionTier(self, value: int):
        return self._set_property(self.PromotionTier.__name__, value)

    def PubliclyAccessible(self, value: bool):
        return self._set_property(self.PubliclyAccessible.__name__, value)

    def SourceDBInstanceIdentifier(self, value: str):
        return self._set_property(self.SourceDBInstanceIdentifier.__name__, value)

    def SourceRegion(self, value: str):
        return self._set_property(self.SourceRegion.__name__, value)

    def StorageEncrypted(self, value: bool):
        return self._set_property(self.StorageEncrypted.__name__, value)

    def StorageType(self, value: str):
        return self._set_property(self.StorageType.__name__, value)

    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))

    def Timezone(self, value: str):
        return self._set_property(self.Timezone.__name__, value)

    def UseDefaultProcessorFeatures(self, value: bool):
        return self._set_property(self.UseDefaultProcessorFeatures.__name__, value)

    def VPCSecurityGroups(self, *value: str):
        return self._set_property(self.VPCSecurityGroups.__name__, list(value))

