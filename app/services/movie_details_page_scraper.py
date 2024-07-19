import argparse
import time

from bs4 import BeautifulSoup
from selenium import webdriver

from classes.MovieDetails import MovieDetails
from classes.MovieDetailsPage import MovieDetailsPage
from services.generic_page_scraper import scrape_recommendations
from utilities.csv_utility import write
from utilities.json_utility import to_json


def scrape_movie_details(movie_id: str, page_source: str) -> MovieDetails:
    """
    Scrapes the 'details-container' class for specific details not rendered anywhere else.

    Args:
        movie_id (str): the unique identifier for the movie.
        page_source (str): A string or a file-like object representing markup to be parsed.

    Returns:
        MovieDetails: a MovieDetails object.
    """

    soup = BeautifulSoup(page_source, 'html.parser')

    details_container = soup.select_one('.content-container .details-container')

    return MovieDetails(
        movie_id=movie_id,
        movie_name=details_container.select_one('.name-container .label').get_text().strip(),
        movie_genres=details_container.select_one('.genres-container .value').get_text().strip(),
        movie_rating=len(details_container.select('.rating-container .value .fill')),
        movie_votes=int(details_container.select_one('.votes-container .value').get_text().strip().replace(',', '')),
        movie_link_imdb=details_container.select('.icon-container a')[0]['href'],
        movie_link_google=details_container.select('.icon-container a')[1]['href'],
    )


def scrape(driver: webdriver.Chrome, movie_id: str) -> MovieDetailsPage:
    """
    Scrapes the 'wheelerrecommends' movie details page and returns the results as a MovieDetailsPage object.

    Args:
        driver (webdriver): Chrome webdriver instance.
        movie_id (str): the unique identifier for the movie.

    Returns:
        MovieDetailsPage: a MovieDetailsPage object.
    """

    driver.get(f"https://wheelerrecommends.com/?title={movie_id}")
    driver.maximize_window()

    time.sleep(3)

    page_source = driver.page_source

    return MovieDetailsPage(
        page_url=driver.current_url,
        details=scrape_movie_details(movie_id, page_source),
        recommendations=scrape_recommendations(page_source),
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser('movie-details-page-scraper')
    parser.add_argument('movie_id', help='any "movie_id" to build the "details_link" programmatically')

    args = parser.parse_args()

    data = scrape(webdriver.Chrome(), args.movie_id)

    print(to_json(data))

    write(data)
