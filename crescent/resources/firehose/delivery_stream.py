from crescent.core import Resource, Validator
from .elasticsearch_destination_configuration import ElasticsearchDestinationConfiguration
from .extended_s3_destination_configuration import ExtendedS3DestinationConfiguration
from .kinesis_stream_source_configuration import KinesisStreamSourceConfiguration
from .redshift_destination_configuration import RedshiftDestinationConfiguration
from .s3_destination_configuration import S3DestinationConfiguration
from .splunk_destination_configuration import SplunkDestinationConfiguration
from .constants import ModelRequiredProperties, AllowedValues


class DeliveryStream(Resource):
    __TYPE = "AWS::KinesisFirehose::DeliveryStream"

    def __init__(self, id: str):
        super(DeliveryStream, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str, min_length=1, max_length=64, pattern=r"[a-zA-Z0-9_.-]+")
    def DeliveryStreamName(self, delivery_stream_name: str):
        return self._set_property(self.DeliveryStreamName.__name__, delivery_stream_name)

    @Validator.validate(type=str, allowed_values=AllowedValues.DELIVERY_STREAM_TYPE)
    def DeliveryStreamType(self, delivery_stream_type: str):
        return self._set_property(self.DeliveryStreamType.__name__, delivery_stream_type)

    @Validator.validate(type=ElasticsearchDestinationConfiguration, required_properties=ModelRequiredProperties.ELASTICSEARCH_DESTINATION_CONFIGURATION)
    def ElasticsearchDestinationConfiguration(self, elasticsearch_destination_conf: ElasticsearchDestinationConfiguration):
        return self._set_property(self.ElasticsearchDestinationConfiguration.__name__, elasticsearch_destination_conf.__to_dict__())

    @Validator.validate(type=ExtendedS3DestinationConfiguration, required_properties=ModelRequiredProperties.EXTENDED_S3_DESTINATION_CONFIGURATION)
    def ExtendedS3DestinationConfiguration(self, extended_s3_destination_conf: ExtendedS3DestinationConfiguration):
        return self._set_property(self.ExtendedS3DestinationConfiguration.__name__, extended_s3_destination_conf.__to_dict__())

    @Validator.validate(type=KinesisStreamSourceConfiguration, required_properties=ModelRequiredProperties.KINESIS_STREAM_SOURCE_CONFIGURATION)
    def KinesisStreamSourceConfiguration(self, kinesis_stream_source_conf: KinesisStreamSourceConfiguration):
        return self._set_property(self.KinesisStreamSourceConfiguration.__name__, kinesis_stream_source_conf.__to_dict__())

    @Validator.validate(type=RedshiftDestinationConfiguration, required_properties=ModelRequiredProperties.REDSHIFT_DESTINATION_CONFIGURATION)
    def RedshiftDestinationConfiguration(self, redshift_destination_conf: RedshiftDestinationConfiguration):
        return self._set_property(self.RedshiftDestinationConfiguration.__name__, redshift_destination_conf.__to_dict__())

    @Validator.validate(type=S3DestinationConfiguration, required_properties=ModelRequiredProperties.S3_DESTINATION_CONFIGURATION)
    def S3DestinationConfiguration(self, s3_destination_conf: S3DestinationConfiguration):
        return self._set_property(self.S3DestinationConfiguration.__name__, s3_destination_conf.__to_dict__())

    @Validator.validate(type=SplunkDestinationConfiguration, required_properties=ModelRequiredProperties.SPLUNK_DESTINATION_CONFIGURATION)
    def SplunkDestinationConfiguration(self, splunk_destination_conf: SplunkDestinationConfiguration):
        return self._set_property(self.SplunkDestinationConfiguration.__name__, splunk_destination_conf.__to_dict__())
