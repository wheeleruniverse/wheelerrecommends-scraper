import csv
import datetime
import os
import shutil
import uuid

from classes.HomePage import HomePage
from classes.MovieDetailsPage import MovieDetailsPage


def write(page_obj: any) -> str:
    """
    Writes the provided 'page_obj' to a csv.

    Args:
        page_obj (HomePage | MovieDetailsPage): The page object to create filename for.

    Returns:
        str: The absolute path to the recently created csv file.
    """

    if isinstance(page_obj, HomePage):
        return __write_home_page(page_obj)

    elif isinstance(page_obj, MovieDetailsPage):
        return __write_movie_details_page(page_obj)

    else:
        raise TypeError("page_obj must be HomePage or MovieDetailsPage")


def __create_file_path(page_obj: any) -> str:
    """
    Creates a file path based on the provided page object.

    Args:
        page_obj (HomePage | MovieDetailsPage): The page object to create filename for.

    Returns:
        str: The created file path.
    """

    if isinstance(page_obj, HomePage):
        datetime_obj = page_obj.datetime
        file_suffix = "home_page"

    elif isinstance(page_obj, MovieDetailsPage):
        datetime_obj = page_obj.datetime
        file_suffix = "movie_details_page"

    else:
        raise TypeError("page_obj must be HomePage or MovieDetailsPage")

    tmp_dir_path = __create_tmp_dir(datetime_obj)

    time_str = datetime_obj.strftime("%H%M%S")

    return f"{tmp_dir_path}/{time_str}_{file_suffix}.csv"


def __create_tmp_dir(datetime_obj: datetime.datetime) -> str:
    """
    Creates a temporary directory. If the directory already exists it will be recursively deleted beforehand.

    Args:
        datetime_obj (datetime.datetime): The datetime object that will be used to create subdirectories within
        the temporary directory.

    Returns:
        str: The path to a temporary directory that was either created, or re-created,
        with subdirectories for the provided year/month/day of the datetime object provided.
    """

    root_dir = "/tmp/scraper"
    if os.path.exists(root_dir):
        shutil.rmtree(root_dir)

    date_str = datetime_obj.strftime("%Y/%m/%d")

    tmp_dir_path = f"{root_dir}/{date_str}"

    os.makedirs(tmp_dir_path)

    return tmp_dir_path


def __write_home_page(home_page: HomePage) -> str:
    """
    Writes the provided HomePage object to a csv.

    Args:
        home_page (HomePage): The HomePage object to write.

    Returns:
        str: The absolute path to the recently created csv file.
    """

    file_path = __create_file_path(home_page)

    with open(file_path, 'w') as f:
        csv_writer = csv.writer(f, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_ALL)
        csv_writer.writerow([
            'id',
            'page_timestamp',
            'page_url',
            'view_more_clicks',
            'recommendation_id',
            'recommendation_idx',
            'recommendation_link_details',
            'recommendation_name',
            'recommendation_poster',
            'recommendation_timestamp',
        ])

        for movie in home_page.recommendations:
            csv_writer.writerow([
                uuid.uuid4().hex,
                home_page.datetime.isoformat(),
                home_page.page_url,
                home_page.view_more_clicks,
                movie.movie_id,
                movie.movie_idx,
                movie.movie_link_details,
                movie.movie_name,
                movie.movie_poster,
                movie.datetime.isoformat(),
            ])

    return file_path


def __write_movie_details_page(movie_details_page: MovieDetailsPage) -> str:
    """
    Writes the provided MovieDetailsPage object to a csv.

    Args:
        movie_details_page (MovieDetailsPage): The MovieDetailsPage object to write.

    Returns:
        str: The absolute path to the recently created csv file.
    """

    file_path = __create_file_path(movie_details_page)

    with open(file_path, 'w') as f:
        csv_writer = csv.writer(f, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_ALL)
        csv_writer.writerow([
            'id',
            'page_timestamp',
            'page_url',
            'details_genres',
            'details_id',
            'details_link_imdb',
            'details_link_google',
            'details_name',
            'details_rating',
            'details_votes',
            'recommendation_id',
            'recommendation_idx',
            'recommendation_link_details',
            'recommendation_name',
            'recommendation_poster',
            'recommendation_timestamp',
        ])

        for movie in movie_details_page.recommendations:
            csv_writer.writerow([
                uuid.uuid4().hex,
                movie_details_page.datetime.isoformat(),
                movie_details_page.page_url,
                movie_details_page.details.movie_genres,
                movie_details_page.details.movie_id,
                movie_details_page.details.movie_link_imdb,
                movie_details_page.details.movie_link_google,
                movie_details_page.details.movie_name,
                movie_details_page.details.movie_rating,
                movie_details_page.details.movie_votes,
                movie.movie_id,
                movie.movie_idx,
                movie.movie_link_details,
                movie.movie_name,
                movie.movie_poster,
                movie.datetime.isoformat(),
            ])

    return file_path
