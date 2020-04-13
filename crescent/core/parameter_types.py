class Constants:
    LIST_TYPE_FMT = "List<{}>"
    AWS_TYPE_FMT = "AWS::{}"
    AWS_EC2_TYPE = "EC2"
    AWS_EC2_TYPE_AVAILABILITY_ZONE_NAME = ["AvailabilityZone", "Name"]
    AWS_EC2_TYPE_IMAGE_ID = ["Image", "Id"]
    AWS_EC2_TYPE_INSTANCE_ID = ["Instance", "Id"]
    AWS_EC2_TYPE_KEY_PAIR_KEY_NAME = ["KeyPair", "KeyName"]
    AWS_EC2_TYPE_SECURITY_GROUP_NAME = ["SecurityGroup", "GroupName"]
    AWS_EC2_TYPE_SECURITY_GROUP_ID = ["SecurityGroup", "Id"]
    AWS_EC2_TYPE_SUBNET_ID = ["Subnet", "Id"]
    AWS_EC2_TYPE_VOLUME_ID = ["Volume", "Id"]
    AWS_EC2_TYPE_VPC_ID = ["VPC", "Id"]
    AWS_ROUTE53_TYPE_HOSTEDZONE_ID = ["Route53", "HostedZone", "Id"]
    AWS_SSM_VALUE_TYPE_FMT = "Value<{}>"
    AWS_SSM_PARAMETER_TYPE = ["SSM", "Parameter"]
    AWS_SSM_NAME_TYPE = "Name"


# -------------------------- STANDARD TYPES --------------------------
class ParameterType(str):
    def __new__(cls, value):
        return super().__new__(cls, value)


class ListParameterType(ParameterType):
    def __new__(cls, value):
        return super(ListParameterType, cls).__new__(cls, Constants.LIST_TYPE_FMT.format(value))


class String(ParameterType):
    def __new__(cls, *args, **kwargs):
        return super(String, cls).__new__(cls, cls.__name__)


class Number(ParameterType):
    def __new__(cls, *args, **kwargs):
        return super(Number, cls).__new__(cls, cls.__name__)


class NumberList(ListParameterType):
    def __new__(cls, *args, **kwargs):
        return super(NumberList, cls).__new__(cls, Number.__name__)


class CommaDelimitedList(ParameterType):
    def __new__(cls, *args, **kwargs):
        return super(CommaDelimitedList, cls).__new__(cls, cls.__name__)


# ------------------------ AWS SPECIFIC TYPES ------------------------
class AwsParameterType(ParameterType):
    def __new__(cls, *value):
        return super(AwsParameterType, cls).__new__(cls, Constants.AWS_TYPE_FMT.format("::".join(list(value))))


class AwsEc2Type(AwsParameterType):
    def __new__(cls, *value):
        return super(AwsEc2Type, cls).__new__(cls, Constants.AWS_EC2_TYPE, *value)


class AvailabilityZoneName(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(AvailabilityZoneName, cls).__new__(cls, *Constants.AWS_EC2_TYPE_AVAILABILITY_ZONE_NAME)


class ImageId(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(ImageId, cls).__new__(cls, *Constants.AWS_EC2_TYPE_IMAGE_ID)


class InstanceId(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(InstanceId, cls).__new__(cls, *Constants.AWS_EC2_TYPE_INSTANCE_ID)


class KeyPairKeyName(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(KeyPairKeyName, cls).__new__(cls, *Constants.AWS_EC2_TYPE_KEY_PAIR_KEY_NAME)


class SecurityGroupName(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(SecurityGroupName, cls).__new__(cls, *Constants.AWS_EC2_TYPE_SECURITY_GROUP_NAME)


class SecurityGroupId(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(SecurityGroupId, cls).__new__(cls, *Constants.AWS_EC2_TYPE_SECURITY_GROUP_ID)


class SubnetId(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(SubnetId, cls).__new__(cls, *Constants.AWS_EC2_TYPE_SUBNET_ID)


class VolumeId(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(VolumeId, cls).__new__(cls, *Constants.AWS_EC2_TYPE_VOLUME_ID)


class VPCId(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(VPCId, cls).__new__(cls, *Constants.AWS_EC2_TYPE_VPC_ID)


class Route53HostedZoneId(AwsParameterType):
    def __new__(cls, *args, **kwargs):
        return super(Route53HostedZoneId, cls).__new__(cls, *Constants.AWS_ROUTE53_TYPE_HOSTEDZONE_ID)


class AvailabilityZoneNameList(ListParameterType):
    def __new__(cls, *args, **kwargs):
        return super(AvailabilityZoneNameList, cls).__new__(cls, AvailabilityZoneName())


class ImageIdList(ListParameterType):
    def __new__(cls, *args, **kwargs):
        return super(ImageIdList, cls).__new__(cls, ImageId())


class InstanceIdList(ListParameterType):
    def __new__(cls, *args, **kwargs):
        return super(InstanceIdList, cls).__new__(cls, InstanceId())


class SecurityGroupNameList(ListParameterType):
    def __new__(cls, *args, **kwargs):
        return super(SecurityGroupNameList, cls).__new__(cls, SecurityGroupName())


class SecurityGroupIdList(ListParameterType):
    def __new__(cls, *args, **kwargs):
        return super(SecurityGroupIdList, cls).__new__(cls, SecurityGroupId())


class SubnetIdList(ListParameterType):
    def __new__(cls, *args, **kwargs):
        return super(SubnetIdList, cls).__new__(cls, SubnetId())


class VolumeIdList(ListParameterType):
    def __new__(cls, *args, **kwargs):
        return super(VolumeIdList, cls).__new__(cls, VolumeId())


class VPCIdList(ListParameterType):
    def __new__(cls, *args, **kwargs):
        return super(VPCIdList, cls).__new__(cls, VPCId())


class Route53HostedZoneIdList(ListParameterType):
    def __new__(cls, *args, **kwargs):
        return super(Route53HostedZoneIdList, cls).__new__(cls, Route53HostedZoneId())


class AwsSsmType(AwsParameterType):
    def __new__(cls, *value):
        return super(AwsSsmType, cls).__new__(cls, *Constants.AWS_SSM_PARAMETER_TYPE, *value)


class Name(AwsSsmType):
    def __new__(cls, *args, **kwargs):
        return super(Name, cls).__new__(cls, Constants.AWS_SSM_NAME_TYPE)


class Value(AwsSsmType):
    def __new__(cls, _type: ParameterType):
        return super(Value, cls).__new__(cls, Constants.AWS_SSM_VALUE_TYPE_FMT.format(_type))
# ----------------------------------------------------------------------------------------------------------------------


class ParameterTypes:
    String = String()
    Number = Number()
    NumberList = NumberList()
    CommaDelimitedList = CommaDelimitedList()

    class Aws:
        class Ec2:
            AvailabilityZoneName = AvailabilityZoneName()
            ImageId = ImageId()
            InstanceId = InstanceId()
            KeyPairKeyName = KeyPairKeyName()
            SecurityGroupName = SecurityGroupName()
            SecurityGroupId = SecurityGroupId()
            SubnetId = SubnetId()
            VolumeId = VolumeId()
            VPCId = VPCId()
            Route53HostedZoneId = Route53HostedZoneId()
            AvailabilityZoneNameList = AvailabilityZoneNameList()
            ImageIdList = ImageIdList()
            InstanceIdList = InstanceIdList()
            SecurityGroupNameList = SecurityGroupNameList()
            SecurityGroupIdList = SecurityGroupIdList()
            SubnetIdList = SubnetIdList()
            VolumeIdList = VolumeIdList()
            VPCIdList = VPCIdList()
            Route53HostedZoneIdList = Route53HostedZoneIdList()

        class Ssm:
            Name = Name()

            @staticmethod
            def Value(_type: ParameterType): return Value(_type)
