from pyformation.core import Resource, Validator
from .elasticsearch_destination_configuration import ElasticsearchDestinationConfiguration
from .extended_s3_destination_configuration import ExtendedS3DestinationConfiguration
from .kinesis_stream_source_configuration import KinesisStreamSourceConfiguration
from .redshift_destination_configuration import RedshiftDestinationConfiguration
from .s3_destination_configuration import S3DestinationConfiguration
from .splunk_destination_configuration import SplunkDestinationConfiguration


class DeliveryStream(Resource):
    __TYPE = "AWS::KinesisFirehose::DeliveryStream"

    def __init__(self, id: str):
        super(DeliveryStream, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def DeliveryStreamName(self, value: str):
        return self._set_property(self.DeliveryStreamName.__name__, value)

    @Validator.validate(type=str)
    def DeliveryStreamType(self, value: str):
        return self._set_property(self.DeliveryStreamType.__name__, value)

    @Validator.validate(type=ElasticsearchDestinationConfiguration)
    def ElasticsearchDestinationConfiguration(self, value: ElasticsearchDestinationConfiguration):
        return self._set_property(self.ElasticsearchDestinationConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=ExtendedS3DestinationConfiguration)
    def ExtendedS3DestinationConfiguration(self, value: ExtendedS3DestinationConfiguration):
        return self._set_property(self.ExtendedS3DestinationConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=KinesisStreamSourceConfiguration)
    def KinesisStreamSourceConfiguration(self, value: KinesisStreamSourceConfiguration):
        return self._set_property(self.KinesisStreamSourceConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=RedshiftDestinationConfiguration)
    def RedshiftDestinationConfiguration(self, value: RedshiftDestinationConfiguration):
        return self._set_property(self.RedshiftDestinationConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=S3DestinationConfiguration)
    def S3DestinationConfiguration(self, value: S3DestinationConfiguration):
        return self._set_property(self.S3DestinationConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=SplunkDestinationConfiguration)
    def SplunkDestinationConfiguration(self, value: SplunkDestinationConfiguration):
        return self._set_property(self.SplunkDestinationConfiguration.__name__, value.__to_dict__())
