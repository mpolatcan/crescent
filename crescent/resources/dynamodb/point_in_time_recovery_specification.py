from crescent.core import Model


class PointInTimeRecoverySpecification(Model):
    def __init__(self):
        super(PointInTimeRecoverySpecification, self).__init__()

    def PointInTimeRecoveryEnabled(self, enabled: bool):
        return self._set_field(self.PointInTimeRecoveryEnabled.__name__, enabled)
