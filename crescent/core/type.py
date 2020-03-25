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
class Type(str):
    def __new__(cls, value):
        return super().__new__(cls, value)


class ListType(Type):
    def __new__(cls, value):
        return super(ListType, cls).__new__(cls, LIST_TYPE_FMT.format(value))


class String(Type):
    def __new__(cls, *args, **kwargs):
        return super(String, cls).__new__(cls, cls.__name__)


class Number(Type):
    def __new__(cls, *args, **kwargs):
        return super(Number, cls).__new__(cls, cls.__name__)


class NumberList(ListType):
    def __new__(cls, *args, **kwargs):
        return super(NumberList, cls).__new__(cls, Number.__name__)


class CommaDelimitedList(Type):
    def __new__(cls, *args, **kwargs):
        return super(CommaDelimitedList, cls).__new__(cls, cls.__name__)


# ------------------------ AWS SPECIFIC TYPES ------------------------
class AwsType(Type):
    def __new__(cls, *value):
        return super(AwsType, cls).__new__(cls, AWS_TYPE_FMT.format("::".join(list(value))))


class AwsEc2Type(AwsType):
    def __new__(cls, *value):
        return super(AwsEc2Type, cls).__new__(cls, AWS_EC2_TYPE, *value)


class AvailabilityZoneName(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(AvailabilityZoneName, cls).__new__(cls, *AWS_EC2_TYPE_AVAILABILITY_ZONE_NAME)


class ImageId(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(ImageId, cls).__new__(cls, *AWS_EC2_TYPE_IMAGE_ID)


class InstanceId(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(InstanceId, cls).__new__(cls, *AWS_EC2_TYPE_INSTANCE_ID)


class KeyPairKeyName(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(KeyPairKeyName, cls).__new__(cls, *AWS_EC2_TYPE_KEY_PAIR_KEY_NAME)


class SecurityGroupName(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(SecurityGroupName, cls).__new__(cls, *AWS_EC2_TYPE_SECURITY_GROUP_NAME)


class SecurityGroupId(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(SecurityGroupId, cls).__new__(cls, *AWS_EC2_TYPE_SECURITY_GROUP_ID)


class SubnetId(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(SubnetId, cls).__new__(cls, *AWS_EC2_TYPE_SUBNET_ID)


class VolumeId(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(VolumeId, cls).__new__(cls, *AWS_EC2_TYPE_VOLUME_ID)


class VPCId(AwsEc2Type):
    def __new__(cls, *args, **kwargs):
        return super(VPCId, cls).__new__(cls, *AWS_EC2_TYPE_VPC_ID)


class Route53HostedZoneId(AwsType):
    def __new__(cls, *args, **kwargs):
        return super(Route53HostedZoneId, cls).__new__(cls, *AWS_ROUTE53_TYPE_HOSTEDZONE_ID)


class AvailabilityZoneNameList(ListType):
    def __new__(cls, *args, **kwargs):
        return super(AvailabilityZoneNameList, cls).__new__(cls, AvailabilityZoneName())


class ImageIdList(ListType):
    def __new__(cls, *args, **kwargs):
        return super(ImageIdList, cls).__new__(cls, ImageId())


class InstanceIdList(ListType):
    def __new__(cls, *args, **kwargs):
        return super(InstanceIdList, cls).__new__(cls, InstanceId())


class SecurityGroupNameList(ListType):
    def __new__(cls, *args, **kwargs):
        return super(SecurityGroupNameList, cls).__new__(cls, SecurityGroupName())


class SecurityGroupIdList(ListType):
    def __new__(cls, *args, **kwargs):
        return super(SecurityGroupIdList, cls).__new__(cls, SecurityGroupId())


class SubnetIdList(ListType):
    def __new__(cls, *args, **kwargs):
        return super(SubnetIdList, cls).__new__(cls, SubnetId())


class VolumeIdList(ListType):
    def __new__(cls, *args, **kwargs):
        return super(VolumeIdList, cls).__new__(cls, VolumeId())


class VPCIdList(ListType):
    def __new__(cls, *args, **kwargs):
        return super(VPCIdList, cls).__new__(cls, VPCId())


class Route53HostedZoneIdList(ListType):
    def __new__(cls, *args, **kwargs):
        return super(Route53HostedZoneIdList, cls).__new__(cls, Route53HostedZoneId())


class AwsSsmType(AwsType):
    def __new__(cls, *value):
        return super(AwsSsmType, cls).__new__(cls, *AWS_SSM_PARAMETER_TYPE, *value)


class Name(AwsSsmType):
    def __new__(cls, *args, **kwargs):
        return super(Name, cls).__new__(cls, AWS_SSM_NAME_TYPE)


class Value(AwsSsmType):
    def __new__(cls, _type: Type):
        return super(Value, cls).__new__(cls, AWS_SSM_VALUE_TYPE_FMT.format(_type))
# ----------------------------------------------------------------------------------------------------------------------


class TypesFactory:
    @staticmethod
    def String():
        return String()

    @staticmethod
    def Number():
        return Number()

    @staticmethod
    def NumberList():
        return NumberList()

    @staticmethod
    def CommaDelimitedList():
        return CommaDelimitedList()

    class __AwsTypesFactory:
        class __Ec2TypesFactory:
            @staticmethod
            def AvailabilityZoneName():
                return AvailabilityZoneName()

            @staticmethod
            def ImageId():
                return ImageId()

            @staticmethod
            def InstanceId():
                return InstanceId()

            @staticmethod
            def KeyPairKeyName():
                return KeyPairKeyName()

            @staticmethod
            def SecurityGroupName():
                return SecurityGroupName()

            @staticmethod
            def SecurityGroupId():
                return SecurityGroupId()

            @staticmethod
            def SubnetId():
                return SubnetId()

            @staticmethod
            def VolumeId():
                return VolumeId()

            @staticmethod
            def VPCId():
                return VPCId()

            @staticmethod
            def Route53HostedZoneId():
                return Route53HostedZoneId()

            @staticmethod
            def AvailabilityZoneNameList():
                return AvailabilityZoneNameList()

            @staticmethod
            def ImageIdList():
                return ImageIdList()

            @staticmethod
            def InstanceIdList():
                return InstanceIdList()

            @staticmethod
            def SecurityGroupNameList():
                return SecurityGroupNameList()

            @staticmethod
            def SecurityGroupIdList():
                return SecurityGroupIdList()

            @staticmethod
            def SubnetIdList():
                return SubnetIdList()

            @staticmethod
            def VolumeIdList():
                return VolumeIdList()

            @staticmethod
            def VPCIdList():
                return VPCIdList()

            @staticmethod
            def Route53HostedZoneIdList():
                return Route53HostedZoneIdList()

        class __SsmTypesFactory:
            @staticmethod
            def Name():
                return Name()

            @staticmethod
            def Value(_type: Type):
                return Value(_type)

        ec2 = __Ec2TypesFactory
        ssm = __SsmTypesFactory

    aws = __AwsTypesFactory


types = TypesFactory
aws_types = types.aws
aws_ec2_types = aws_types.ec2
aws_ssm_types = aws_types.ssm

