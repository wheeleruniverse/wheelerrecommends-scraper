import json


class MovieDetails:
    """
    An object that contains complete data that represents a Movie.
    """

    def __init__(
            self,
            movie_id=None,
            movie_name=None,
            movie_genres=None,
            movie_rating=None,
            movie_votes=None,
            movie_link_imdb=None,
            movie_link_google=None,
    ):
        """
        Creates a Movie object.

        Args:
            movie_id (str): the unique identifier for the movie.
            movie_name (str): the movie name and year.
            movie_genres (str): the movie genres.
            movie_rating (str): the movie rating.
            movie_votes (str): the number of votes a movie received for it's rating.
            movie_link_imdb (str): an IMDb link for the movie.
            movie_link_google (str): a Google link for the movie.
        """

        self.movie_id = movie_id
        self.movie_name = movie_name
        self.movie_genres = movie_genres
        self.movie_rating = movie_rating
        self.movie_votes = movie_votes
        self.movie_link_imdb = movie_link_imdb
        self.movie_link_google = movie_link_google

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4, sort_keys=True)
