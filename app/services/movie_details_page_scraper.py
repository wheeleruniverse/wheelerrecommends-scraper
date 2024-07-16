import argparse
import json
import time

from bs4 import BeautifulSoup
from selenium import webdriver

from app.classes.Movie import Movie
from app.classes.MovieDetails import MovieDetails
from app.classes.MovieDetailsPage import MovieDetailsPage


def scrape_movie_details(movie_id: str, soup: BeautifulSoup):
    """
    Scrapes the 'details-container' class for specific details not rendered anywhere else.

    Args:
        movie_id (str): the unique identifier for the movie.
        soup (BeautifulSoup): BeautifulSoup object.

    Returns:
        MovieDetails: a MovieDetails object.
    """

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


def scrape(movie_id: str):
    """
    Scrapes the 'wheelerrecommends' movie details page and returns the results as a MovieDetailsPage object.

    Args:
        movie_id (str): the unique identifier for the movie.

    Returns:
        MovieDetailsPage: a MovieDetailsPage object.
    """

    # create driver
    driver = webdriver.Chrome()

    # load and maximize website
    driver.get(f"https://wheelerrecommends.com/?title={movie_id}")
    driver.maximize_window()

    # wait because website is dynamically loaded
    time.sleep(3)

    # scrape the website
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    posters = soup.select('.content-container .movies-container:not(.hidden) .poster')

    movies = []
    for idx, poster in enumerate(posters):
        movies.append(
            Movie(
                movie_id=poster['id'],
                movie_idx=idx,
                movie_name=poster.select_one('.movie-name').get_text(),
                movie_poster=poster.select_one('img')['src'],
                details_link=poster.select_one('a')['href'],
            ))

    return MovieDetailsPage(
        page_url=driver.current_url,
        details=scrape_movie_details(movie_id, soup),
        recommendations=movies
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser('movie-details-page-scraper')
    parser.add_argument('movie_id', help='any "movie_id" to build the "details_link" programmatically')

    args = parser.parse_args()

    data = scrape(args.movie_id)
    print(json.dumps(data, default=lambda o: o.__dict__, indent=4, sort_keys=True))
