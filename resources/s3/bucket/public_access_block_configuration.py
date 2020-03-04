from resources.shared.base_model import BaseModel


class PublicAccessBlockConfiguration(BaseModel):
    __PROPERTY_BLOCK_PUBLIC_ACLS = "BlockPublicAcls"
    __PROPERTY_BLOCK_PUBLIC_POLICY = "BlockPublicPolicy"
    __PROPERTY_IGNORE_PUBLIC_ACLS = "IgnorePublicAcls"
    __PROPERTY_RESTRICT_PUBLIC_BUCKETS = "RestrictPublicBuckets"

    def block_public_acls(self, value: bool):
        return self._add_field(self.__PROPERTY_BLOCK_PUBLIC_ACLS, value)

    def block_public_policy(self, value: bool):
        return self._add_field(self.__PROPERTY_BLOCK_PUBLIC_POLICY, value)

    def ignore_public_acls(self, value: bool):
        return self._add_field(self.__PROPERTY_IGNORE_PUBLIC_ACLS, value)

    def restrict_public_buckets(self, value: bool):
        return self._add_field(self.__PROPERTY_RESTRICT_PUBLIC_BUCKETS, value)
