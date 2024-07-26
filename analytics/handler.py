
import json
import pyodbc

connection_string = (
    'AuthenticationType=Default Credentials;'
    'AwsRegion=us-east-1;'
    'Catalog=AwsDataCatalog;'
    'DRIVER={Amazon Athena ODBC (x64)};'
    'S3OutputLocation=s3://wheelerrecommends-scraper-logs/;'
    'Schema=wheelerrecommends-scraper-database;'
)


def main(event, context):
    print(f"analytics-BC8521DA1A874F4E9A6DB5: event: {event}, context: {context}")
    return __query_home_page()


def __query_home_page():
    """
    Connects to the database and executes the SQL statement provided.

    Returns:
       str: JSON representation of the SQL query results.
    """

    print(f"analytics-AD29A3EF2A874F8E9A6CZ1: connection_string: {connection_string}")

    connection = pyodbc.connect(connection_string)
    print(f"analytics-722A353D70D14993BF96C5: connection: {connection}")

    cursor = connection.cursor()
    print(f"analytics-FBC89168C99045BBB8EF17: cursor: {cursor}")

    try:
        cursor.execute(
            'select'
            ' id,'
            ' page_timestamp,'
            ' page_url,'
            ' view_more_clicks,'
            ' recommendation_id,'
            ' recommendation_idx,'
            ' recommendation_link_details,'
            ' recommendation_name,'
            ' recommendation_poster,'
            ' recommendation_timestamp'
            ' from home_page'
            ' limit 10;'
        )
        cursor_records = list(cursor)
        print(f"analytics-7CC2586752304CF68452B4: retrieved {len(cursor_records)} record(s) from cursor")

    finally:
        cursor.close()
        print(f"analytics-50F66759700547E4B0F334: cursor closed")

        connection.close()
        print(f"analytics-99CEE18CA2C74F498E70BD: connection closed")

    print(f"analytics-8E2911A304154F298B3489: mapping cursor_records to output_records")
    output_records = []
    for row in cursor_records:
        output_records.append({
            'id': row[0],
            'page_timestamp': row[1],
            'page_url': row[2],
            'view_more_clicks': row[3],
            'recommendation_id': row[4],
            'recommendation_idx': row[5],
            'recommendation_link_details': row[6],
            'recommendation_name': row[7],
            'recommendation_poster': row[8],
            'recommendation_timestamp': row[9],
        })

    print(f"analytics-D9AF1C7D6F2B45CD9AAC31: mapping output_records to json")
    return json.dumps(output_records, indent=4, sort_keys=True)


def __override_connection_string(profile=None):
    """
    Updates the global "connection_string" to use the "AuthenticationType=IAM Profile" and "AWSProfile".
    Note: Intended for local testing only.

    Args:
        profile (str): The name of the profile to use.
    """

    global connection_string
    connection_string = (
        'AuthenticationType=IAM Profile;'
        f'AWSProfile={profile};'
        'AwsRegion=us-east-1;'
        'Catalog=AwsDataCatalog;'
        'DRIVER={Amazon Athena ODBC (x64)};'
        'S3OutputLocation=s3://wheelerrecommends-scraper-logs/;'
        'Schema=wheelerrecommends-scraper-database;'
    )


if __name__ == '__main__':

    __override_connection_string('wheelers-websites')

    print(f"__query_home_page:\n{__query_home_page()}")
