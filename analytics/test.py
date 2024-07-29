
import boto3

# local testing with AWS profile
# session = boto3.session.Session(profile_name='wheelers-websites')
# athena_client = session.client('athena', region_name='us-east-1')

athena_client = boto3.client('athena', region_name='us-east-1')


def main(event, context):
    print(f"event: {event}, context: {context}")
    print(
        athena_client.start_query_execution(
            QueryString='select * from home_page limit 10;',
            QueryExecutionContext={
                'Catalog': 'AwsDataCatalog',
                'Database': 'wheelerrecommends-scraper-database'
            },
            ResultConfiguration={
                'AclConfiguration': {
                    'S3AclOption': 'BUCKET_OWNER_FULL_CONTROL'
                },
                'EncryptionConfiguration': {
                    'EncryptionOption': 'SSE_S3'
                },
                'OutputLocation': 's3://wheelerrecommends-scraper-logs/',
            },
            WorkGroup='primary',
            ResultReuseConfiguration={
                'ResultReuseByAgeConfiguration': {
                    'Enabled': False,
                }
            }
        ))


if __name__ == '__main__':
    main(None, None)
