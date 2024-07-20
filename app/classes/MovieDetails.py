from utilities.json_utility import to_json


class MovieDetails:
    """
    An object that contains complete data that represents a Movie.
    """

    def __init__(
            self,
            movie_id: str,
            movie_name: str,
            movie_genres: str,
            movie_rating: int,
            movie_votes: int,
            movie_link_imdb: str,
            movie_link_google: str,
    ):
        """
        Creates a MovieDetails object.

        Args:
            movie_id (str): the unique identifier for the movie.
            movie_name (str): the movie name and year.
            movie_genres (str): the movie genres.
            movie_rating (int): the movie rating.
            movie_votes (int): the number of votes a movie received for it's rating.
            movie_link_imdb (str): an IMDb link for the movie.
            movie_link_google (str): a Google link for the movie.

        Returns:
            MovieDetails: a MovieDetails object.
        """

        self.movie_id = movie_id
        self.movie_name = movie_name
        self.movie_genres = movie_genres
        self.movie_rating = movie_rating
        self.movie_votes = movie_votes
        self.movie_link_imdb = movie_link_imdb
        self.movie_link_google = movie_link_google

    def __str__(self) -> str:
        """
        Returns:
            str: a JSON string representation of the MovieDetails object.
        """
        return to_json(self)
