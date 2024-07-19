
from bs4 import BeautifulSoup
from typing import List

from classes.Movie import Movie


def scrape_recommendations(page_source: str) -> List[Movie]:
    """
    Scrapes the current 'page_source' for movie recommendations by looking for the 'poster' class.

    Args:
        page_source (str): A string or a file-like object representing markup to be parsed.

    Returns:
        List[Movie]: movie recommendations found.
    """

    soup = BeautifulSoup(page_source, 'html.parser')

    posters = soup.select('.content-container .movies-container:not(.hidden) .poster')

    recommendations = []
    for idx, poster in enumerate(posters):
        recommendations.append(
            Movie(
                movie_id=poster['id'],
                movie_idx=idx,
                movie_link_details=poster.select_one('a')['href'],
                movie_name=poster.select_one('.movie-name').get_text(),
                movie_poster=poster.select_one('img')['src'],
            ))

    return recommendations
