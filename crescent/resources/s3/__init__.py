from .access_point import AccessPointFactory
from .bucket import BucketFactory
from .bucket_policy import BucketPolicyFactory


class S3:
    AccessPoint = AccessPointFactory
    Bucket = BucketFactory
    BucketPolicy = BucketPolicyFactory


__all__ = ["S3"]
