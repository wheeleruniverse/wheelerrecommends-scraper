import json


class MovieDetailsPage:
    """
    An object that contains data found on the MovieDetails page.
    """

    def __init__(
            self,
            page_url=None,
            details=None,
            recommendations=None,
    ):
        """
        Creates a MovieDetailsPage object.

        Args:
            page_url (str): the url of the page.
            details (MovieDetails): a MovieDetails object.
            recommendations (Movie[]): a Movie[] object.
        """

        self.page_url = page_url
        self.details = details
        self.recommendations = recommendations

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4, sort_keys=True)
