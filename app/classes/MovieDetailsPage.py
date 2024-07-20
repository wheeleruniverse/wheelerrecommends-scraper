
import datetime

from typing import List

from classes.Movie import Movie
from classes.MovieDetails import MovieDetails
from utilities.json_utility import to_json


class MovieDetailsPage:
    """
    An object that contains data found on the MovieDetails page.
    """

    def __init__(
            self,
            page_url: str,
            details: MovieDetails,
            recommendations: List[Movie],
    ):
        """
        Creates a MovieDetailsPage object.

        Args:
            page_url (str): the url of the page.
            details (MovieDetails): a MovieDetails object.
            recommendations (List[Movie]): a List[Movie] object.

        Returns:
            MovieDetailsPage: a MovieDetailsPage object.
        """

        self.datetime = datetime.datetime.now()
        self.page_url = page_url
        self.details = details
        self.recommendations = recommendations

    def __str__(self) -> str:
        """
        Returns:
            str: a JSON string representation of the MovieDetailsPage object.
        """
        return to_json(self)
