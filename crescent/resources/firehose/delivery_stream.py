from crescent.core import Resource
from .elasticsearch_destination_configuration import ElasticsearchDestinationConfiguration
from .extended_s3_destination_configuration import ExtendedS3DestinationConfiguration
from .kinesis_stream_source_configuration import KinesisStreamSourceConfiguration
from .redshift_destination_configuration import RedshiftDestinationConfiguration
from .s3_destination_configuration import S3DestinationConfiguration
from .splunk_destination_configuration import SplunkDestinationConfiguration
from .constants import AllowedValues


class DeliveryStream(Resource):
    __TYPE = "AWS::KinesisFirehose::DeliveryStream"

    def __init__(self, id: str):
        super(DeliveryStream, self).__init__(
            id=id,
            type=self.__TYPE,
            min_length={self.DeliveryStreamName.__name__: 1},
            max_length={self.DeliveryStreamName.__name__: 64},
            pattern={self.DeliveryStreamName.__name__: r"[a-zA-Z0-9_.-]+"},
            allowed_values={self.DeliveryStreamType.__name__: AllowedValues.DELIVERY_STREAM_TYPE}
        )

    def DeliveryStreamName(self, delivery_stream_name: str):
        return self._set_property(self.DeliveryStreamName.__name__, delivery_stream_name)

    def DeliveryStreamType(self, delivery_stream_type: str):
        return self._set_property(self.DeliveryStreamType.__name__, delivery_stream_type)

    def ElasticsearchDestinationConfiguration(self, elasticsearch_destination_conf: ElasticsearchDestinationConfiguration):
        return self._set_property(self.ElasticsearchDestinationConfiguration.__name__, elasticsearch_destination_conf)

    def ExtendedS3DestinationConfiguration(self, extended_s3_destination_conf: ExtendedS3DestinationConfiguration):
        return self._set_property(self.ExtendedS3DestinationConfiguration.__name__, extended_s3_destination_conf)

    def KinesisStreamSourceConfiguration(self, kinesis_stream_source_conf: KinesisStreamSourceConfiguration):
        return self._set_property(self.KinesisStreamSourceConfiguration.__name__, kinesis_stream_source_conf)

    def RedshiftDestinationConfiguration(self, redshift_destination_conf: RedshiftDestinationConfiguration):
        return self._set_property(self.RedshiftDestinationConfiguration.__name__, redshift_destination_conf)

    def S3DestinationConfiguration(self, s3_destination_conf: S3DestinationConfiguration):
        return self._set_property(self.S3DestinationConfiguration.__name__, s3_destination_conf)

    def SplunkDestinationConfiguration(self, splunk_destination_conf: SplunkDestinationConfiguration):
        return self._set_property(self.SplunkDestinationConfiguration.__name__, splunk_destination_conf)
