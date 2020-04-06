from crescent.core import Model


class PublicAccessBlockConfiguration(Model):
    def BlockPublicAcls(self, block_public_acls: bool):
        return self._set_field(self.BlockPublicAcls.__name__, block_public_acls)

    def BlockPublicPolicy(self, block_public_policy: bool):
        return self._set_field(self.BlockPublicPolicy.__name__, block_public_policy)

    def IgnorePublicAcls(self, ignore_public_acls: bool):
        return self._set_field(self.IgnorePublicAcls.__name__, ignore_public_acls)

    def RestrictPublicBuckets(self, restrict_public_buckets: bool):
        return self._set_field(self.RestrictPublicBuckets.__name__, restrict_public_buckets)
