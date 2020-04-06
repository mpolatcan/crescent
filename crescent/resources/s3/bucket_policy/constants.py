from crescent.core.constants import get_values


class _RequiredProperties:
    class BucketPolicy:
        BUCKET = "Bucket"
        POLICY_DOCUMENT = "PolicyDocument"


# --------------------------------------------------


class ResourceRequiredProperties:
    BUCKET_POLICY = get_values(_RequiredProperties.BucketPolicy)
