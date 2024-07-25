
import json
import pyodbc

connection_string = 'athena_odbc'


def main(event, context):
    print(f"scraper-BC8521DA1A874F4E9A6DB5: wheelerrecommends-scraper-analytics: event: {event}, context: {context}")
    results = __query_home_page()
    print(results)


def __query_home_page():
    """
    Connects to the database and executes the SQL statement provided.

    Returns:
       str: JSON representation of the SQL query results.
    """

    cursor = __get_cursor()
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

    data = []
    for row in cursor:
        data.append({
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

    return json.dumps(data, indent=4, sort_keys=True)


def __get_cursor():
    """
    Connects to the database with the global "connection_string".

    Returns:
        Cursor: a Cursor object to the database.
    """

    connection = pyodbc.connect(connection_string)
    return connection.cursor()


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

    main(None, None)

