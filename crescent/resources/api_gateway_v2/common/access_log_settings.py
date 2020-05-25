from crescent.core import Model


class AccessLogSettings(Model):
    def __init__(self):
        super(AccessLogSettings, self).__init__()

    # FIXME Add correct arn type to function definition
    def DestinationArn(self, destination_arn: str):
        return self._set_field(self.DestinationArn.__name__, destination_arn)

    def Format(self, format: str):
        return self._set_field(self.Format.__name__, format)
