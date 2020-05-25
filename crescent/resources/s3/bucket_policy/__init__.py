from .bucket_policy import BucketPolicy


class BucketPolicyFactory:
    @staticmethod
    def Create(id: str): return BucketPolicy(id)


__all__ = ["BucketPolicyFactory"]
