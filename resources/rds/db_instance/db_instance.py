from resources.shared.base_cf_resource_model import BaseCloudFormationResourceModel


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



    def __init__(self):
        super(DBInstance, self).__init__(type=self.__TYPE)

