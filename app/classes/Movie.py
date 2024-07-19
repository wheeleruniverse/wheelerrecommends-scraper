
import datetime

from utilities.json_utility import to_json


class Movie:
    """
    An object that contains partial data that represents a Movie.
    """

    def __init__(
            self,
            movie_id: str,
            movie_idx: int,
            movie_link_details: str,
            movie_name: str,
            movie_poster: str,
    ):
        """
        Creates a Movie object.

        Args:
            movie_id (str): the unique identifier for the movie.
            movie_idx (int): the current index the movie was found at.
            movie_link_details (str): the link to the details page.
            movie_name (str): a truncated version of the movie name and year.
            movie_poster (str): the poster filename.

        Returns:
            Movie: a Movie object.
        """

        self.datetime = datetime.datetime.now()
        self.movie_id = movie_id
        self.movie_idx = movie_idx
        self.movie_link_details = movie_link_details
        self.movie_name = movie_name
        self.movie_poster = movie_poster

    def __str__(self):
        return to_json(self)
