from resources.shared import BaseCloudFormationResourceModel
from resources.firehose import (
    ElasticsearchDestinationConfiguration,
    ExtendedS3DestinationConfiguration,
    KinesisStreamSourceConfiguration,
    RedshiftDestinationConfiguration,
    S3DestinationConfiguration,
    SplunkDestinationConfiguration
)


class DeliveryStream(BaseCloudFormationResourceModel):
    __TYPE = "AWS::KinesisFirehose::DeliveryStream"
    __PROPERTY_DELIVERY_STREAM_NAME = "DeliveryStreamName"
    __PROPERTY_DELIVERY_STREAM_TYPE = "DeliveryStreamType"
    __PROPERTY_ELASTICSEARCH_DESTINATION_CONFIGURATION = "ElasticsearchDestinationConfiguration"
    __PROPERTY_EXTENDED_S3_DESTINATION_CONFIGURATION = "ExtendedS3DestinationConfiguration"
    __PROPERTY_KINESIS_STREAM_SOURCE_CONFIGURATION = "KinesisStreamSourceConfiguration"
    __PROPERTY_REDSHIFT_DESTINATION_CONFIGURATION = "RedshiftDestinationConfiguration"
    __PROPERTY_S3_DESTINATON_CONFIGURATION = "S3DestinationConfiguration"
    __PROPERTY_SPLUNK_DESTINATION_CONFIGURATION = "SplunkDestinationConfiguration"

    def __init__(self):
        super(DeliveryStream, self).__init__(type=self.__TYPE)

    def delivery_stream_name(self, value: str):
        return self._add_property_field(self.__PROPERTY_DELIVERY_STREAM_NAME, value)

    def delivery_stream_type(self, value: str):
        return self._add_property_field(self.__PROPERTY_DELIVERY_STREAM_TYPE, value)

    def elasticsearch_destination_configuration(self, value: ElasticsearchDestinationConfiguration):
        return self._add_property_field(self.__PROPERTY_ELASTICSEARCH_DESTINATION_CONFIGURATION, value.create())

    def extended_s3_destination_configuration(self, value: ExtendedS3DestinationConfiguration):
        return self._add_property_field(self.__PROPERTY_EXTENDED_S3_DESTINATION_CONFIGURATION, value.create())

    def kinesis_stream_source_configuration(self, value: KinesisStreamSourceConfiguration):
        return self._add_property_field(self.__PROPERTY_KINESIS_STREAM_SOURCE_CONFIGURATION, value.create())

    def redshift_destination_configuration(self, value: RedshiftDestinationConfiguration):
        return self._add_property_field(self.__PROPERTY_REDSHIFT_DESTINATION_CONFIGURATION, value.create())

    def s3_destination_configuration(self, value: S3DestinationConfiguration):
        return self._add_property_field(self.__PROPERTY_S3_DESTINATON_CONFIGURATION, value.create())

    def splunk_destination_configuration(self, value: SplunkDestinationConfiguration):
        return self._add_property_field(self.__PROPERTY_SPLUNK_DESTINATION_CONFIGURATION, value.create())
