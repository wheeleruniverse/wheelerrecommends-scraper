import json


class Movie:
    """
    An object that contains partial data that represents a Movie.
    """

    def __init__(
            self,
            movie_id=None,
            movie_idx=None,
            movie_name=None,
            movie_poster=None,
            details_link=None,
    ):
        """
        Creates a Movie object.

        Args:
            movie_id (str): the unique identifier for the movie.
            movie_idx (int): the current index the movie was found at.
            movie_name (str): a truncated version of the movie name and year.
            movie_poster (str): the poster filename.
            details_link (str): the link to the details page.
        """

        self.movie_id = movie_id
        self.movie_idx = movie_idx
        self.movie_name = movie_name
        self.movie_poster = movie_poster
        self.details_link = details_link

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4, sort_keys=True)
