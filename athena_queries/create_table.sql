CREATE EXTERNAL TABLE IF NOT EXISTS enron_spam_data (
  subject string,
  message string,
  label int
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = '1'
) LOCATION 's3://enron-spam-detection-data/processed/';
