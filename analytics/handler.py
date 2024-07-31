
import datetime
import pyodbc

from enum import Enum

connection_string = (
    'AuthenticationType=Default Credentials;'
    'AwsRegion=us-east-1;'
    'Catalog=AwsDataCatalog;'
    'DRIVER={Amazon Athena ODBC (x64)};'
    'S3OutputLocation=s3://wheelerrecommends-scraper-logs/;'
    'Schema=wheelerrecommends-scraper-database;'
)


class Page(Enum):
    HOME = 1
    MOVIE_DETAILS = 2


def main(event, context):
    print(f"analytics-BC8521DA1A874F4E9A6DB5: event: {event}, context: {context}")

    query_strings = event['queryStringParameters'] if 'queryStringParameters' in event else {}

    page = query_strings['page'] if 'page' in query_strings else Page.HOME

    limit = query_strings['limit'] if 'limit' in query_strings else 10
    limit = limit if limit < 101 else 100
    if limit > 100:
        limit = 100

    return {
        'body': __query(page, limit),
        'date': datetime.datetime.now().isoformat(),
        'request': {
          'page': page.value,
          'limit': limit,
        }
    }


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


def __query(page, limit):
    print(f"analytics-AD29A3EF2A874F8E9A6CZ1: connection_string: {connection_string}, page: {page}, limit: {limit}")

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    print(f"analytics-722A353D70D14993BF96C5: connection established")

    try:
        match page:
            case Page.HOME:
                records = __query_home_page(cursor, limit)
            case Page.MOVIE_DETAILS:
                records = __query_movie_details_page(cursor, limit)
            case _:
                records = []

        print(f"analytics-7CC2586752304CF68452B4: retrieved {len(records)} record(s) from cursor")
        return records

    finally:
        cursor.close()
        connection.close()
        print(f"analytics-99CEE18CA2C74F498E70BD: connection closed")


def __query_home_page(cursor, limit):
    """
    Connects to the database and executes the SQL statement provided.

    Args:
        cursor (pyodbc.Cursor): the database cursor to execute against.
        limit (int): the maximum number of records to return.

    Returns:
       dict: mapped SQL query results from the cursor.
    """

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
        ' recommendation_timestamp,'
        ' year,'
        ' month,'
        ' day'
        ' from home_page'
        ' where day = cast(day(current_date) as varchar)'
        ' order by page_timestamp desc'
        ' limit {0};'.format(limit)
    )

    output_records = []
    for row in cursor:
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
            'year': row[10],
            'month': row[11],
            'day': row[12],
        })

    return output_records


def __query_movie_details_page(cursor, limit):
    """
    Connects to the database and executes the SQL statement provided.

    Args:
        cursor (pyodbc.Cursor): the database cursor to execute against.
        limit (int): the maximum number of records to return.

    Returns:
       dict: mapped SQL query results from the cursor.
    """

    cursor.execute(
        'select'
        ' id,'
        ' page_timestamp,'
        ' page_url,'
        ' details_genres,'
        ' details_id,'
        ' details_link_imdb,'
        ' details_link_google,'
        ' details_name,'
        ' details_rating,'
        ' details_votes,'
        ' recommendation_id,'
        ' recommendation_idx,'
        ' recommendation_link_details,'
        ' recommendation_name,'
        ' recommendation_poster,'
        ' recommendation_timestamp,'
        ' year,'
        ' month,'
        ' day'
        ' from movie_details_page'
        ' where day = cast(day(current_date) as varchar)'
        ' order by page_timestamp desc'
        ' limit {0};'.format(limit)
    )

    output_records = []
    for row in cursor:
        output_records.append({
            'id': row[0],
            'page_timestamp': row[1],
            'page_url': row[2],
            'details_genres': row[3],
            'details_id': row[4],
            'details_link_imdb': row[5],
            'details_link_google': row[6],
            'details_name': row[7],
            'details_rating': row[8],
            'details_votes': row[9],
            'recommendation_id': row[10],
            'recommendation_idx': row[11],
            'recommendation_link_details': row[12],
            'recommendation_name': row[13],
            'recommendation_poster': row[14],
            'recommendation_timestamp': row[15],
            'year': row[16],
            'month': row[17],
            'day': row[18],
        })

    return output_records


if __name__ == '__main__':

    __override_connection_string('wheelers-websites')

    print(f"__query(Page.HOME): {__query(page=Page.HOME, limit=1)}")
    print(f"__query(Page.MOVIE_DETAILS): {__query(page=Page.MOVIE_DETAILS, limit=1)}")
