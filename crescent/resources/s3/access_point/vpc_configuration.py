from crescent.core import Model


class VpcConfiguration(Model):
    def VpcId(self, vpc_id: str):
        return self._set_field(self.VpcId.__name__, vpc_id)
